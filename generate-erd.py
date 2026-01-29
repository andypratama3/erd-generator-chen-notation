import re
import uuid
import os
import sys
from lxml import etree
from collections import defaultdict, deque

# ======================================================
# IMPORT CONFIGURATION FROM database.py
# ======================================================
try:
    from database import (
        SQL_FILE as DEFAULT_SQL_FILE,
        OUTPUT_FILE as DEFAULT_OUTPUT_FILE,
        DIAGRAM_NAME as DEFAULT_DIAGRAM_NAME,
        COLORS,
        ENTITY_STYLE,
        ATTRIBUTE_STYLE,
        ATTRIBUTE_PK_STYLE,
        RELATIONSHIP_STYLE,
        LINE_STYLE,
        RELATION_LINE_STYLE,
        RELATION_LINE_STYLE_ONE,
        LAYOUT,
        SKIP_COLUMNS,
        MXGRAPH_CONFIG,
        DYNAMIC_HEIGHT,
        CARDINALITY_LABEL,
        JUNCTION_TABLE_RULES,
        ATTRIBUTE_PLACEMENT
    )
    CONFIG_LOADED = True
except ImportError:
    print("❌ Error: database.py tidak ditemukan!")
    print("Silakan buat file database.py terlebih dahulu.")
    sys.exit(1)

def uid():
    return str(uuid.uuid4())

def build_style_string(style_dict, base_type="entity"):
    """Convert style dictionary to draw.io style string"""
    base_styles = {
        "entity": "shape=rectangle;whiteSpace=wrap;html=1;",
        "attribute": "ellipse;whiteSpace=wrap;html=1;",
        "relationship": "rhombus;whiteSpace=wrap;html=1;",
        "line": "",
        "text": "text;html=1;"
    }
    
    style_str = base_styles.get(base_type, "")
    for key, value in style_dict.items():
        style_str += f"{key}={value};"
    
    if base_type in ["entity", "attribute", "relationship"]:
        style_str += "align=center;verticalAlign=middle;"
    
    return style_str

# ======================================================
# INTERACTIVE INPUT
# ======================================================
print("=" * 70)
print("🚀 ERD Generator - Chen Notation (Improved Layout)")
print("=" * 70)
print("✅ Config loaded from database.py\n")

available_files = [f for f in os.listdir('.') if f.endswith('.sql')]

if not available_files:
    print("❌ Tidak ada file SQL di folder ini!")
    print("Silakan letakkan file SQL di folder ini")
    sys.exit(1)

print("📂 File SQL yang tersedia:")
for i, f in enumerate(available_files, 1):
    default_marker = " (default)" if f == DEFAULT_SQL_FILE else ""
    print(f"   {i}. {f}{default_marker}")

print("\n🔍 Pilih file SQL:")
print(f"   Tekan Enter untuk default: {DEFAULT_SQL_FILE}")

try:
    choice = input(f"Masukkan nomor (1-{len(available_files)}) atau Enter: ").strip()
    
    if not choice:
        SQL_FILE = DEFAULT_SQL_FILE
        print(f"✅ Menggunakan default: {SQL_FILE}")
    else:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(available_files):
            print("❌ Pilihan tidak valid!")
            sys.exit(1)
        SQL_FILE = available_files[idx]
        print(f"✅ File dipilih: {SQL_FILE}")
except ValueError:
    print("❌ Input tidak valid!")
    sys.exit(1)

print(f"\n💾 Nama output file (default: {DEFAULT_OUTPUT_FILE}):")
output_name = input("Masukkan nama (atau tekan Enter): ").strip()

if not output_name:
    OUTPUT_FILE = DEFAULT_OUTPUT_FILE
    print(f"✅ Menggunakan default: {OUTPUT_FILE}")
else:
    if not output_name.endswith('.drawio'):
        output_name += ".drawio"
    OUTPUT_FILE = output_name
    print(f"✅ Output: {OUTPUT_FILE}")

print(f"\n📊 Nama diagram (default: {DEFAULT_DIAGRAM_NAME}):")
diagram_name = input("Masukkan nama (atau tekan Enter): ").strip()

if not diagram_name:
    DIAGRAM_NAME = DEFAULT_DIAGRAM_NAME
    print(f"✅ Menggunakan default: {DIAGRAM_NAME}")
else:
    DIAGRAM_NAME = diagram_name
    print(f"✅ Diagram: {DIAGRAM_NAME}")

print("\n" + "=" * 70)
print("⚙️  Memproses...")
print("=" * 70 + "\n")

# ======================================================
# LOAD SQL
# ======================================================
print("📖 Membaca file SQL...")
try:
    with open(SQL_FILE, encoding="utf-8") as f:
        sql = f.read()
    print(f"✅ File dibaca: {SQL_FILE}")
except FileNotFoundError:
    print(f"❌ File tidak ditemukan: {SQL_FILE}")
    sys.exit(1)

# ======================================================
# PARSE DATABASE
# ======================================================
print("🔍 Parsing database...")
tables = {}
foreign_keys = defaultdict(list)
primary_keys = {}

blocks = re.findall(
    r'CREATE TABLE `(\w+)`\s*\((.*?)\)\s*ENGINE',
    sql,
    re.S
)

for table, body in blocks:
    cols = []
    fks = []
    pk = None

    for line in body.splitlines():
        line = line.strip()
        if line.startswith("`"):
            col = line.split("`")[1]
            cols.append(col)
        if line.startswith("PRIMARY KEY"):
            m = re.search(r'`(\w+)`', line)
            if m:
                pk = m.group(1)
        if "FOREIGN KEY" in line:
            fk = re.search(r'FOREIGN KEY \(`(\w+)`\) REFERENCES `(\w+)`', line)
            if fk:
                fks.append((fk.group(1), fk.group(2)))

    tables[table] = cols
    foreign_keys[table] = fks
    primary_keys[table] = pk

print(f"✅ Ditemukan {len(tables)} tabel")

# ======================================================
# DETECT M:N
# ======================================================
print("🔗 Mendeteksi junction tables (M:N)...")
junction_tables = set()

for table, fks in foreign_keys.items():
    if len(fks) >= JUNCTION_TABLE_RULES["min_foreign_keys"]:
        non_fk = [c for c in tables[table] if c not in [f[0] for f in fks] and c not in SKIP_COLUMNS]
        if len(non_fk) <= JUNCTION_TABLE_RULES["max_non_fk_columns"]:
            junction_tables.add(table)

print(f"✅ Ditemukan {len(junction_tables)} junction tables")

# ======================================================
# COUNT ATTRIBUTES PER TABLE
# ======================================================
print("📊 Menghitung attribute per tabel...")
attr_count = {}

for table, cols in tables.items():
    fk_cols = {f[0] for f in foreign_keys[table]}
    count = 0
    for col in cols:
        if col.endswith("_id") and col in fk_cols:
            continue
        if col in SKIP_COLUMNS:
            continue
        count += 1
    attr_count[table] = count

# ======================================================
# IMPROVED LAYERING ALGORITHM
# ======================================================
print("📈 Menghitung layer layout dengan algoritma improved...")

def calculate_layers_improved(tables, foreign_keys, junction_tables):
    """
    Improved layering algorithm dengan:
    1. Topological sorting untuk dependency
    2. Grouping berdasarkan relationship count
    3. Balancing untuk distribusi yang lebih rata
    """
    layers = defaultdict(list)
    in_degree = {}
    out_degree = {}
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    # Build graph
    for table in tables:
        in_degree[table] = 0
        out_degree[table] = 0
    
    for table, fks in foreign_keys.items():
        for fk_col, ref_table in fks:
            graph[ref_table].append(table)
            reverse_graph[table].append(ref_table)
            in_degree[table] += 1
            out_degree[ref_table] += 1
    
    # Topological sort dengan level assignment
    level_map = {}
    queue = deque()
    
    # Start with tables that have no dependencies
    for table in tables:
        if in_degree[table] == 0:
            level_map[table] = 0
            queue.append(table)
    
    while queue:
        table = queue.popleft()
        current_level = level_map[table]
        
        for dependent in graph[table]:
            if dependent not in level_map:
                # Assign level based on maximum parent level + 1
                parent_levels = [level_map.get(p, 0) for p in reverse_graph[dependent]]
                new_level = max(parent_levels) + 1 if parent_levels else current_level + 1
                level_map[dependent] = new_level
                
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
    
    # Handle any remaining tables (circular dependencies)
    for table in tables:
        if table not in level_map:
            if foreign_keys[table]:
                max_ref_level = max(level_map.get(fk[1], 0) for fk in foreign_keys[table] if fk[1] in level_map)
                level_map[table] = max_ref_level + 1
            else:
                level_map[table] = 0
    
    # Group into layers
    for table, level in level_map.items():
        layers[level].append(table)
    
    # Balance layers - redistribute if a layer is too crowded
    max_per_layer = 4
    balanced_layers = defaultdict(list)
    layer_idx = 0
    
    for level in sorted(layers.keys()):
        current_batch = [t for t in layers[level] if t not in junction_tables]
        
        while len(current_batch) > max_per_layer:
            balanced_layers[layer_idx] = current_batch[:max_per_layer]
            current_batch = current_batch[max_per_layer:]
            layer_idx += 1
        
        if current_batch:
            balanced_layers[layer_idx] = current_batch
            layer_idx += 1
    
    # Rebuild level_map
    new_level_map = {}
    for level, tables_in_level in balanced_layers.items():
        for table in tables_in_level:
            new_level_map[table] = level
    
    return balanced_layers, new_level_map

layers, level_map = calculate_layers_improved(tables, foreign_keys, junction_tables)

# ======================================================
# CALCULATE POSITIONS - IMPROVED
# ======================================================
print("📐 Menghitung posisi entitas dengan spacing optimal...")
positions = {}

for level in sorted(layers.keys()):
    level_tables = [t for t in layers[level] if t not in junction_tables]
    level_tables.sort()
    
    if not level_tables:
        continue
    
    # Calculate dynamic height based on max attributes in this layer
    max_attr = max(attr_count.get(t, 5) for t in level_tables)
    
    # Calculate layer height
    attr_left = (max_attr + 1) // 2
    attr_right = max_attr - attr_left
    max_side = max(attr_left, attr_right)
    
    dynamic_layer_height = max(
        DYNAMIC_HEIGHT["base"] + 
        DYNAMIC_HEIGHT["top_padding"] + 
        (max_side * DYNAMIC_HEIGHT["attribute_spacing"]) + 
        DYNAMIC_HEIGHT["bottom_padding"],
        DYNAMIC_HEIGHT["min_layer_height"]
    )
    
    # Center entities horizontally if there are few tables
    num_tables = len(level_tables)
    total_width = num_tables * LAYOUT["col_width"]
    start_x = LAYOUT["padding_x"]
    
    if num_tables <= 3:
        # Center alignment for sparse layers
        start_x = LAYOUT["padding_x"] + (3 - num_tables) * LAYOUT["col_width"] // 4
    
    for idx, table in enumerate(level_tables):
        x = start_x + idx * LAYOUT["col_width"]
        y = LAYOUT["padding_y"] + level * dynamic_layer_height
        positions[table] = (x, y)

print(f"✅ {len(positions)} entitas diposisikan")

# ======================================================
# INIT mxGraph
# ======================================================
print("🎨 Membuat mxGraph XML...")
mxfile = etree.Element("mxfile", host=MXGRAPH_CONFIG["host"])
diagram = etree.SubElement(mxfile, "diagram", name=DIAGRAM_NAME)
model = etree.SubElement(diagram, "mxGraphModel")
model.set("dx", MXGRAPH_CONFIG["dx"])
model.set("dy", MXGRAPH_CONFIG["dy"])
root = etree.SubElement(model, "root")

etree.SubElement(root, "mxCell", id="0")
etree.SubElement(root, "mxCell", id="1", parent="0")

entity_ids = {}

# ======================================================
# CREATE ENTITIES WITH IMPROVED ATTRIBUTE PLACEMENT
# ======================================================
print("🏢 Membuat entitas dengan atribut...")

for table in sorted(tables.keys()):
    if table in junction_tables or table not in positions:
        continue
    
    x, y = positions[table]
    eid = uid()
    entity_ids[table] = eid

    ent = etree.SubElement(
        root, "mxCell",
        id=eid,
        value=table,
        style=build_style_string(ENTITY_STYLE, "entity"),
        vertex="1",
        parent="1"
    )

    g = etree.SubElement(ent, "mxGeometry")
    g.set("x", str(x))
    g.set("y", str(y))
    g.set("width", str(LAYOUT["entity_width"]))
    g.set("height", str(LAYOUT["entity_height"]))
    g.set("as", "geometry")

    # -------- IMPROVED ATTRIBUTE PLACEMENT --------
    LEFT_X = x + LAYOUT["attr_left_x"]
    RIGHT_X = x + LAYOUT["entity_width"] + LAYOUT["attr_right_x"]
    
    start_y = y + LAYOUT["entity_height"] + ATTRIBUTE_PLACEMENT["start_offset"]
    ay_left = start_y
    ay_right = start_y
    
    fk_cols = {f[0] for f in foreign_keys[table]}
    col_list = sorted(tables[table])
    
    # Filter columns
    display_cols = []
    for col_name in col_list:
        if col_name.endswith("_id") and col_name in fk_cols:
            continue
        if col_name in SKIP_COLUMNS:
            continue
        display_cols.append(col_name)
    
    # Distribute attributes using alternating strategy
    for idx, col_name in enumerate(display_cols):
        if ATTRIBUTE_PLACEMENT["strategy"] == "alternating":
            # Zigzag pattern: left, right, left, right...
            if idx % 2 == 0:
                ax, ay = LEFT_X, ay_left
                ay_left += LAYOUT["attr_spacing"]
            else:
                ax, ay = RIGHT_X, ay_right
                ay_right += LAYOUT["attr_spacing"]
        elif ATTRIBUTE_PLACEMENT["strategy"] == "balanced":
            # Split evenly
            if idx < len(display_cols) // 2:
                ax, ay = LEFT_X, ay_left
                ay_left += LAYOUT["attr_spacing"]
            else:
                ax, ay = RIGHT_X, ay_right
                ay_right += LAYOUT["attr_spacing"]
        else:  # left-priority
            if idx < ATTRIBUTE_PLACEMENT["max_per_side"]:
                ax, ay = LEFT_X, ay_left
                ay_left += LAYOUT["attr_spacing"]
            else:
                ax, ay = RIGHT_X, ay_right
                ay_right += LAYOUT["attr_spacing"]

        is_pk = col_name == primary_keys[table]
        style = build_style_string(
            ATTRIBUTE_PK_STYLE if is_pk else ATTRIBUTE_STYLE,
            "attribute"
        )

        aid = uid()
        attr = etree.SubElement(
            root, "mxCell",
            id=aid,
            value=col_name,
            style=style,
            vertex="1",
            parent="1"
        )

        ga = etree.SubElement(attr, "mxGeometry")
        ga.set("x", str(ax))
        ga.set("y", str(ay))
        ga.set("width", str(LAYOUT["attr_width"]))
        ga.set("height", str(LAYOUT["attr_height"]))
        ga.set("as", "geometry")

        edge = etree.SubElement(
            root, "mxCell",
            id=uid(),
            edge="1",
            source=aid,
            target=eid,
            style=build_style_string(LINE_STYLE, "line"),
            parent="1"
        )
        ge = etree.SubElement(edge, "mxGeometry")
        ge.set("relative", "1")
        ge.set("as", "geometry")

# ======================================================
# HELPER FUNCTIONS
# ======================================================
def add_cardinality_label(text, x, y):
    cid = uid()
    cell = etree.SubElement(
        root, "mxCell",
        id=cid,
        value=text,
        style=f"text;html=1;align=center;verticalAlign=middle;fontSize={CARDINALITY_LABEL['fontSize']};fontStyle={CARDINALITY_LABEL['fontStyle']};fillColor=#ffffff;strokeColor=none;",
        vertex="1",
        parent="1"
    )
    g = etree.SubElement(cell, "mxGeometry")
    g.set("x", str(int(x + CARDINALITY_LABEL['offset_x'])))
    g.set("y", str(int(y + CARDINALITY_LABEL['offset_y'])))
    g.set("width", str(CARDINALITY_LABEL['width']))
    g.set("height", str(CARDINALITY_LABEL['height']))
    g.set("as", "geometry")

# ======================================================
# CREATE RELATIONSHIPS - 1:N WITH ARROWS
# ======================================================
print("💎 Membuat relasi 1:N dengan panah...")

for table, fks in foreign_keys.items():
    if table not in positions or table in junction_tables:
        continue

    for fk_col, target_table in fks:
        if target_table not in positions or target_table not in entity_ids:
            continue
        if table not in entity_ids:
            continue

        ex, ey = positions[table]
        px, py = positions[target_table]
        
        ex_center = ex + LAYOUT["entity_width"] // 2
        ey_center = ey + LAYOUT["entity_height"] // 2
        px_center = px + LAYOUT["entity_width"] // 2
        py_center = py + LAYOUT["entity_height"] // 2
        
        # Calculate relationship position
        midx = (ex_center + px_center) / 2
        midy = (ey_center + py_center) / 2
        
        rx = int(midx - LAYOUT["relationship_width"] // 2)
        ry = int(midy - LAYOUT["relationship_height"] // 2 + LAYOUT["relationship_offset_y"])
        
        rid = uid()
        rel = etree.SubElement(
            root, "mxCell",
            id=rid,
            value="memiliki",
            style=build_style_string(RELATIONSHIP_STYLE, "relationship"),
            vertex="1",
            parent="1"
        )
        
        g = etree.SubElement(rel, "mxGeometry")
        g.set("x", str(rx))
        g.set("y", str(ry))
        g.set("width", str(LAYOUT["relationship_width"]))
        g.set("height", str(LAYOUT["relationship_height"]))
        g.set("as", "geometry")
        
        # Edge from child (Many) to relationship - WITH ARROW
        edge1 = etree.SubElement(
            root, "mxCell",
            id=uid(),
            edge="1",
            source=entity_ids[table],
            target=rid,
            style=build_style_string(RELATION_LINE_STYLE, "line"),  # Dengan panah
            parent="1"
        )
        ge1 = etree.SubElement(edge1, "mxGeometry")
        ge1.set("relative", "1")
        ge1.set("as", "geometry")
        
        # Edge from parent (One) to relationship - NO ARROW
        edge2 = etree.SubElement(
            root, "mxCell",
            id=uid(),
            edge="1",
            source=entity_ids[target_table],
            target=rid,
            style=build_style_string(RELATION_LINE_STYLE_ONE, "line"),  # Tanpa panah
            parent="1"
        )
        ge2 = etree.SubElement(edge2, "mxGeometry")
        ge2.set("relative", "1")
        ge2.set("as", "geometry")
        
        # Add cardinality labels
        m_x = (ex_center + (rx + LAYOUT["relationship_width"] // 2)) / 2
        m_y = (ey_center + (ry + LAYOUT["relationship_height"] // 2)) / 2 - 15
        add_cardinality_label("N", m_x, m_y)
        
        one_x = (px_center + (rx + LAYOUT["relationship_width"] // 2)) / 2
        one_y = (py_center + (ry + LAYOUT["relationship_height"] // 2)) / 2 + 15
        add_cardinality_label("1", one_x, one_y)

# ======================================================
# CREATE M:N RELATIONSHIPS
# ======================================================
print("🔗 Membuat relasi M:N...")

for table, fks in foreign_keys.items():
    if table not in junction_tables or len(fks) < 2:
        continue

    refs = [fk[1] for fk in fks if fk[1] in positions and fk[1] in entity_ids]
    
    if len(refs) >= 2:
        a, b = refs[0], refs[1]
        
        ax, ay = positions[a]
        bx, by = positions[b]
        
        ax_center = ax + LAYOUT["entity_width"] // 2
        ay_center = ay + LAYOUT["entity_height"] // 2
        bx_center = bx + LAYOUT["entity_width"] // 2
        by_center = by + LAYOUT["entity_height"] // 2
        
        midx = (ax_center + bx_center) / 2
        midy = (ay_center + by_center) / 2
        
        rx = int(midx - LAYOUT["relationship_width"] // 2)
        ry = int(midy - LAYOUT["relationship_height"] // 2 + LAYOUT["relationship_offset_y"])
        
        rid = uid()
        rel = etree.SubElement(
            root, "mxCell",
            id=rid,
            value="memiliki",
            style=build_style_string(RELATIONSHIP_STYLE, "relationship"),
            vertex="1",
            parent="1"
        )
        
        g = etree.SubElement(rel, "mxGeometry")
        g.set("x", str(rx))
        g.set("y", str(ry))
        g.set("width", str(LAYOUT["relationship_width"]))
        g.set("height", str(LAYOUT["relationship_height"]))
        g.set("as", "geometry")
        
        # Both edges have arrows for M:N
        for ent in (a, b):
            edge = etree.SubElement(
                root, "mxCell",
                id=uid(),
                edge="1",
                source=entity_ids[ent],
                target=rid,
                style=build_style_string(RELATION_LINE_STYLE, "line"),  # Dengan panah
                parent="1"
            )
            ge = etree.SubElement(edge, "mxGeometry")
            ge.set("relative", "1")
            ge.set("as", "geometry")
            
            ex, ey = positions[ent]
            ex_center = ex + LAYOUT["entity_width"] // 2
            ey_center = ey + LAYOUT["entity_height"] // 2
            m_x = (ex_center + (rx + LAYOUT["relationship_width"] // 2)) / 2
            m_y = (ey_center + (ry + LAYOUT["relationship_height"] // 2)) / 2 - 15
            add_cardinality_label("M", m_x, m_y)

# ======================================================
# SAVE FILE
# ======================================================
print("💾 Menyimpan file...")
tree = etree.ElementTree(mxfile)
tree.write(
    OUTPUT_FILE,
    pretty_print=True,
    xml_declaration=True,
    encoding="UTF-8"
)

non_junction_count = len([t for t in tables if t not in junction_tables])
total_relations = sum(len(fks) for fks in foreign_keys.values())
max_layer = max(level_map.values()) if level_map else 0

print("\n" + "=" * 70)
print("✅ ERD CHEN BERHASIL DIBUAT! (IMPROVED LAYOUT)")
print("=" * 70)
print(f"📊 Total Tabel         : {non_junction_count}")
print(f"🔗 Total Relasi        : {total_relations}")
print(f"📈 Jumlah Layer        : {max_layer + 1}")
print(f"💾 File Output         : {OUTPUT_FILE}")
print("=" * 70)
print("\n🎨 Fitur Baru:")
print("   ✓ Improved layering algorithm")
print("   ✓ Balanced layer distribution")
print("   ✓ Optimized attribute spacing")
print("   ✓ Alternating attribute placement (zigzag)")
print("   ✓ Arrows on relationships (N side)")
print("   ✓ Better relationship positioning")
print("   ✓ Dynamic spacing based on content")
print("=" * 70)
print("\n🎉 Buka di: https://app.diagrams.net")
print("=" * 70)