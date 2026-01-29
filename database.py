# ======================================================
# DATABASE CONFIGURATION
# ======================================================

# Nama file SQL (default - akan di-override jika pilih interactive mode)
SQL_FILE = "database-example.sql"

# Nama file output (default - akan di-override jika pilih interactive mode)
OUTPUT_FILE = "erd-chen-notation.drawio"

# Nama diagram (default - akan di-override jika pilih interactive mode)
DIAGRAM_NAME = "ERD Chen FINAL"

# ======================================================
# STYLING CONFIGURATION
# ======================================================

# Warna
COLORS = {
    "border": "#000000",      # Hitam untuk border
    "fill": "#ffffff",        # Putih untuk fill
    "line": "#000000",        # Hitam untuk garis
}

# Entity styling
ENTITY_STYLE = {
    "strokeWidth": "2",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "12",
    "fontStyle": "1",
    "rounded": "0",
}

# Attribute styling
ATTRIBUTE_STYLE = {
    "strokeWidth": "1",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "9",
    "fontStyle": "0",
}

# Attribute PK styling (double border untuk PK)
ATTRIBUTE_PK_STYLE = {
    "strokeWidth": "2",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "9",
    "fontStyle": "5",  # Bold + Underline
}

# Relationship diamond styling
RELATIONSHIP_STYLE = {
    "strokeWidth": "1.5",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "10",
    "fontStyle": "0",
}

# Line styling - PERBAIKAN: Tambah panah
LINE_STYLE = {
    "strokeWidth": "1.5",
    "strokeColor": COLORS["line"],
    "curved": "0",  # Garis lurus lebih rapi
    "endArrow": "none",
    "endFill": "0",
}

# Line styling untuk relasi (dari entity ke relationship)
RELATION_LINE_STYLE = {
    "strokeWidth": "1.5",
    "strokeColor": COLORS["line"],
    "curved": "0",
    "endArrow": "classic",  # Panah untuk N side
    "endFill": "1",
}

RELATION_LINE_STYLE_ONE = {
    "strokeWidth": "1.5",
    "strokeColor": COLORS["line"],
    "curved": "0",
    "endArrow": "none",  # Tanpa panah untuk 1 side
    "endFill": "0",
}

# ======================================================
# LAYOUT CONFIGURATION - IMPROVED
# ======================================================

LAYOUT = {
    # Padding/margin dari edge canvas
    "padding_x": 200,
    "padding_y": 150,
    
    # Jarak horizontal antar kolom entity
    "col_width": 650,  # Diperbesar dari 500 ke 650
    
    # Ukuran entity box
    "entity_width": 180,   # Diperbesar dari 160
    "entity_height": 50,   # Diperbesar dari 45
    
    # Posisi atribut relatif ke entity
    "attr_left_x": -240,   # Lebih jauh ke kiri (dari -170)
    "attr_right_x": 240,   # Lebih jauh ke kanan (dari 180)
    
    # Ukuran atribut
    "attr_height": 28,     # Diperbesar dari 20
    "attr_width": 140,     # Diperbesar dari 120
    
    # Distribusi atribut
    "attr_per_side": 8,    # Dikurangi dari 12 untuk mengurangi kepadatan
    "attr_spacing": 38,    # Diperbesar dari 32
    
    # Ukuran relationship diamond
    "relationship_width": 110,   # Diperbesar dari 100
    "relationship_height": 65,   # Diperbesar dari 50
    "relationship_offset_y": -20,  # Offset vertikal relationship (negatif = ke atas)
}

# ======================================================
# SKIP COLUMNS CONFIGURATION
# ======================================================

SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
    'remember_token',
    'email_verified_at'
}

# ======================================================
# mxGraph CONFIGURATION
# ======================================================

MXGRAPH_CONFIG = {
    "host": "app.diagrams.net",
    "dx": "1434",
    "dy": "790",
}

# ======================================================
# ADVANCED CONFIGURATION
# ======================================================

# Dynamic height calculation - IMPROVED
DYNAMIC_HEIGHT = {
    "base": 50,                    # Base height entity
    "attribute_spacing": 38,       # Space per attribute
    "bottom_padding": 200,         # Padding bawah (diperbesar dari 150)
    "top_padding": 80,            # Padding atas (diperbesar dari 20)
    "min_layer_height": 400,      # Minimum height per layer
}

# Cardinality label configuration
CARDINALITY_LABEL = {
    "offset_x": -10,
    "offset_y": -10,
    "width": 20,
    "height": 20,
    "fontSize": "12",
    "fontStyle": "1",
}

# Junction table detection rules
JUNCTION_TABLE_RULES = {
    "min_foreign_keys": 2,
    "max_non_fk_columns": 1,  # Selain timestamps
}

# ======================================================
# ATTRIBUTE PLACEMENT STRATEGY
# ======================================================

# Strategi penempatan atribut: "balanced", "left-priority", "alternating"
ATTRIBUTE_PLACEMENT = {
    "strategy": "alternating",  # Distribusi zigzag untuk mengurangi overlap
    "max_per_side": 8,          # Maksimal atribut per sisi
    "start_offset": 15,         # Offset dari bawah entity
}