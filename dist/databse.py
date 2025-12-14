# ======================================================
# DATABASE CONFIGURATION
# ======================================================

# Nama file SQL
SQL_FILE = "database-ansor.sql"

# Nama file output
OUTPUT_FILE = "ANSOR_ERD_CHEN_FINAL.drawio"

# Nama diagram
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
    "strokeWidth": "1",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "11",
    "fontStyle": "1",
    "rounded": "1",
}

# Attribute styling
ATTRIBUTE_STYLE = {
    "strokeWidth": "1",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "7",
    "rounded": "1",
}

# Attribute PK styling
ATTRIBUTE_PK_STYLE = {
    "strokeWidth": "1.5",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "8",
    "fontStyle": "1",
    "rounded": "1",
}

# Relationship diamond styling
RELATIONSHIP_STYLE = {
    "strokeWidth": "1",
    "fillColor": COLORS["fill"],
    "strokeColor": COLORS["border"],
    "fontSize": "8",
    "rounded": "1",
}

# Line styling
LINE_STYLE = {
    "endArrow": "none",
    "strokeWidth": "1",
    "strokeColor": COLORS["line"],
    "curved": "1",
}

# ======================================================
# LAYOUT CONFIGURATION
# ======================================================

LAYOUT = {
    "padding_x": 150,
    "padding_y": 150,
    "col_width": 500,
    "entity_width": 160,
    "entity_height": 45,
    "attr_left_x": -170,
    "attr_right_x": 180,
    "attr_height": 20,
    "attr_width": 120,
    "attr_per_side": 12,
    "attr_spacing": 32,
    "relationship_width": 100,
    "relationship_height": 50,
    "relationship_offset_y": 40,
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
    "dx": "1200",
    "dy": "800",
}