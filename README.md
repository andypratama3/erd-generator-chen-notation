# ERD Generator - Chen Notation

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![HTML](https://img.shields.io/badge/HTML-Standalone-orange)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Aplikasi **Python & HTML** untuk **membuat Entity-Relationship Diagram (ERD)** dalam format **draw.io** dari file SQL database Anda secara **otomatis & cepat**.

Menggunakan **Chen's ER Model** dengan:
- 🏢 **Entity** (Rectangle)
- 📝 **Attribute** (Ellipse)  
- 💎 **Relationship** (Diamond) dengan label "memiliki"
- 🔗 **Cardinality** (1/N/M) dengan panah
- ⚖️ **Smart Layout** dengan collision detection

---

## ☕ Support This Project

Jika project ini membantu Anda, pertimbangkan untuk membeli saya kopi! ☕

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/andypratama3)

**Dukungan Anda sangat berarti untuk pengembangan project ini!** 🙏

---

## 🎉 NEW: HTML Version Available!

Sekarang tersedia **2 versi**:

### 1. **Python Version** (Original)
- ✅ Full-featured dengan advanced layout algorithm
- ✅ Interactive CLI dengan file selection
- ✅ Customizable via `database.py`
- ✅ Best untuk workflow development

### 2. **HTML Version** (NEW! ✨)
- ✅ **Standalone** - buka langsung di browser, no installation!
- ✅ **Drag & drop** SQL file
- ✅ **Improved layout** dengan collision detection
- ✅ **Real-time preview** status
- ✅ **Perfect untuk demo** atau one-time use

---

## 📑 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Versi Python](#-python-version)
  - [Requirements](#-requirements-python)
  - [Instalasi](#-instalasi-python)
  - [Quick Start](#-quick-start-python)
- [Versi HTML](#-html-version)
  - [Quick Start](#-quick-start-html)
  - [Features](#-features-html)
- [Struktur Project](#-struktur-project)
- [Kustomisasi](#-kustomisasi)
- [Workflow Sehari-hari](#-workflow-sehari-hari)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)

---

## ✨ Fitur Utama

### Core Features (Both Versions)
✅ **Parse SQL Otomatis** - Baca file SQL dan ekstrak struktur database  
✅ **Generate ERD Chen** - Buat diagram dengan model Chen yang rapi  
✅ **Support Semua Relasi** - Handle 1:N dan M:N relationships  
✅ **Cardinality Labels** - Tampilkan M, N & 1 secara otomatis  
✅ **Draw.io Format** - Output langsung buka di draw.io  
✅ **Customizable Config** - Edit warna, layout, dan skip columns  
✅ **Cross-Platform** - Jalan di Windows, macOS, dan Linux  

### NEW in Version 2.0 (HTML & Python)
✨ **Improved Layout Algorithm** - Topological sorting dengan layer balancing  
✨ **Collision Detection** - Anti-overlap entities dengan smart positioning  
✨ **Arrow Indicators** - Panah pada N side untuk cardinality yang jelas  
✨ **Alternating Attributes** - Zigzag placement untuk mengurangi overlap  
✨ **Dynamic Spacing** - Spacing otomatis berdasarkan jumlah attribute  
✨ **Layer Balancing** - Maksimal 3-4 tables per layer untuk layout optimal  
✨ **Auto-centering** - Entities tersebar rata dan centered  

---

## 🐍 Python Version

### 💻 Requirements (Python)

#### Software
- **Python 3.7+** (3.8+ recommended)
- **pip** (Python package manager)
- **MySQL/MariaDB** SQL file format

#### Library Dependencies
```
lxml>=4.9.0
```

---

### 🚀 Instalasi (Python)

#### Windows

##### 1. Install Python
Download dan install dari [python.org](https://www.python.org/downloads/)

**PENTING**: Centang "Add Python to PATH" saat instalasi!

##### 2. Verifikasi Instalasi
```cmd
python --version
pip --version
```

##### 3. Clone Repository
```cmd
git clone https://github.com/andypratama3/erd-generator-chen-notation.git
cd erd-generator-chen-notation\dist
```

**Atau download ZIP:**
```cmd
# Download dari GitHub → Download ZIP
# Extract ke folder pilihan Anda
cd path\to\erd-generator-chen-notation\dist
```

##### 4. Install Dependencies
```cmd
pip install -r requirements.txt
```

**Jika ada error**, coba:
```cmd
python -m pip install -r requirements.txt
```

##### 5. Jalankan Script
```cmd
python erd_generator_improved.py
```

---

#### macOS

##### 1. Install Python
**Option A - Menggunakan Homebrew (Recommended):**
```bash
# Install Homebrew jika belum ada
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

**Option B - Download dari python.org:**
Download dari [python.org](https://www.python.org/downloads/macos/)

##### 2. Verifikasi Instalasi
```bash
python3 --version
pip3 --version
```

##### 3. Clone Repository
```bash
git clone https://github.com/andypratama3/erd-generator-chen-notation.git
cd erd-generator-chen-notation/dist
```

##### 4. Install Dependencies
```bash
pip3 install -r requirements.txt
```

**Jika ada permission error:**
```bash
pip3 install --user -r requirements.txt
```

##### 5. Jalankan Script
```bash
python3 erd_generator_improved.py
```

---

#### Linux (Ubuntu/Debian)

```bash
# 1. Install Python
sudo apt update
sudo apt install python3 python3-pip

# 2. Clone Repository
git clone https://github.com/andypratama3/erd-generator-chen-notation.git
cd erd-generator-chen-notation/dist

# 3. Install Dependencies
pip3 install -r requirements.txt

# 4. Jalankan Script
python3 erd_generator_improved.py
```

---

### 🎯 Quick Start (Python)

#### 1. Siapkan File SQL

Letakkan file SQL Anda di folder `dist/`:

```bash
# macOS/Linux
cp /path/to/your/database.sql dist/

# Windows
copy C:\path\to\your\database.sql dist\
```

#### 2. Jalankan Script

```bash
cd dist

# macOS/Linux
python3 erd_generator_improved.py

# Windows
python erd_generator_improved.py
```

#### 3. Ikuti Prompts Interaktif

```
🚀 ERD Generator - Chen Notation (Improved Layout)
======================================================================

📂 File SQL yang tersedia:
   1. database-example.sql (default)
   2. my-database.sql

🔍 Pilih file SQL:
   Tekan Enter untuk default: database-example.sql
Masukkan nomor (1-2) atau Enter: 1
✅ File dipilih: database-example.sql

💾 Nama output file (default: erd-chen-notation.drawio):
Masukkan nama (atau tekan Enter): my-erd-improved
✅ Output: my-erd-improved.drawio

📊 Nama diagram (default: ERD Chen FINAL):
Masukkan nama (atau tekan Enter): 
✅ Menggunakan default: ERD Chen FINAL
```

#### 4. Output

```
======================================================================
✅ ERD CHEN BERHASIL DIBUAT! (IMPROVED LAYOUT)
======================================================================
📊 Total Tabel         : 8
🔗 Total Relasi        : 14
📈 Jumlah Layer        : 3
💾 File Output         : my-erd-improved.drawio
======================================================================

🎨 Fitur Baru:
   ✓ Improved layering algorithm
   ✓ Balanced layer distribution
   ✓ Optimized attribute spacing
   ✓ Alternating attribute placement (zigzag)
   ✓ Arrows on relationships (N side)
   ✓ Better relationship positioning
   ✓ Dynamic spacing based on content
======================================================================

🎉 Buka di: https://app.diagrams.net
======================================================================
```

---

## 🌐 HTML Version

### 🎯 Quick Start (HTML)

#### Option 1: Direct Download

1. Download file `erdgen-chen-improved-v2.html`
2. Buka file di browser (Chrome, Firefox, Safari, Edge)
3. Drag & drop SQL file atau klik "Upload SQL File"
4. Configure output name & diagram name
5. Click "🚀 Generate ERD"
6. Click "💾 Download ERD (.drawio)"

#### Option 2: Clone Repository

```bash
# Clone repository
git clone https://github.com/andypratama3/erd-generator-chen-notation.git
cd erd-generator-chen-notation

# Buka file HTML di browser
# macOS
open erdgen-chen-improved-v2.html

# Linux
xdg-open erdgen-chen-improved-v2.html

# Windows
start erdgen-chen-improved-v2.html
```

### ✨ Features (HTML)

#### 1. **Modern UI/UX** 🎨
- Beautiful gradient background
- Smooth animations
- Drag & drop support
- Real-time status updates
- Responsive design

#### 2. **Smart Upload** 📤
- Drag & drop SQL files
- File size indicator
- Instant validation
- File info preview

#### 3. **Configuration** ⚙️
- Output file name
- Diagram name
- Simple interface

#### 4. **Real-time Processing** ⚡
- Live status updates:
  - 🔍 Parsing SQL file...
  - ✅ Found X tables
  - 🔗 Detected Y junction tables
  - 🎨 Generating ERD diagram...
  - ✅ ERD generated successfully!

#### 5. **Advanced Layout** 📐
- **Improved layering algorithm**
- **Collision detection** - no overlapping entities
- **Smart positioning** - auto-adjustment if collision detected
- **Dynamic spacing** - based on attribute count
- **Layer balancing** - max 3 tables per layer
- **Alternating attributes** - zigzag pattern to reduce overlap
- **Arrow indicators** - clear cardinality (N side has arrow, 1 side no arrow)

#### 6. **Instant Download** 💾
- One-click download
- .drawio format
- Ready to open in draw.io

---

## 📋 Struktur Project

```
erd-generator-chen-notation/
│
├── README.md                           # 📖 Dokumentasi lengkap
├── LICENSE                             # MIT License
│
├── dist/                               # 🐍 Python Version
│   ├── database.py                     # ⚙️ Configuration file
│   ├── erd_generator_improved.py       # 🚀 Main script (improved)
│   ├── requirements.txt                # Python dependencies
│   ├── database-example.sql            # 📄 Sample SQL
│   └── database-ansor.sql              # 📄 Complex SQL sample
│
├── erdgen-chen-improved-v2.html        # 🌐 HTML Version (standalone)
└── erdgen-chen-fixed.html              # 🌐 HTML Version (basic)
```

**Files Description:**

### Python Files
- **`database.py`** - Configuration file untuk customization (warna, layout, spacing)
- **`erd_generator_improved.py`** - Main script dengan improved algorithm
- **`requirements.txt`** - Python dependencies (lxml)

### HTML Files
- **`erdgen-chen-improved-v2.html`** - ⭐ **RECOMMENDED** - Latest version dengan collision detection
- **`erdgen-chen-fixed.html`** - Basic version dengan arrow support

---

## 🔧 Kustomisasi

### Python Version - Edit `database.py`

#### 1. Default Configuration
```python
SQL_FILE = "database-example.sql"
OUTPUT_FILE = "erd-chen-notation.drawio"
DIAGRAM_NAME = "ERD Chen FINAL"
```

#### 2. Colors
```python
COLORS = {
    "border": "#000000",
    "fill": "#ffffff",
    "line": "#000000",
}
```

**Preset Warna:**

**Modern Dark:**
```python
COLORS = {
    "border": "#2C3E50",
    "fill": "#ECF0F1",
    "line": "#34495E",
}
```

**Fresh Green:**
```python
COLORS = {
    "border": "#27AE60",
    "fill": "#E8F8F5",
    "line": "#1E8449",
}
```

#### 3. Layout Configuration
```python
LAYOUT = {
    "padding_x": 250,           # Horizontal padding
    "padding_y": 200,           # Vertical padding
    "col_width": 800,           # Distance between columns
    "entity_width": 180,        # Entity box width
    "entity_height": 50,        # Entity box height
    "attr_left_x": -260,        # Left attributes offset
    "attr_right_x": 260,        # Right attributes offset
    "attr_width": 140,          # Attribute width
    "attr_height": 28,          # Attribute height
    "attr_spacing": 42,         # Spacing between attributes
    "relationship_width": 110,  # Diamond width
    "relationship_height": 65,  # Diamond height
    "relationship_offset_y": -20, # Vertical offset
}
```

#### 4. Skip Columns
```python
SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
    'remember_token',
    'email_verified_at',
    # Add your custom columns to skip
}
```

#### 5. Advanced Settings
```python
# Dynamic Height
DYNAMIC_HEIGHT = {
    "base": 50,
    "attribute_spacing": 42,
    "bottom_padding": 250,
    "top_padding": 100,
    "min_layer_height": 500,
}

# Attribute Placement Strategy
ATTRIBUTE_PLACEMENT = {
    "strategy": "alternating",  # zigzag pattern
    "max_per_side": 8,
    "start_offset": 15,
}

# Junction Table Rules
JUNCTION_TABLE_RULES = {
    "min_foreign_keys": 2,
    "max_non_fk_columns": 1,
}
```

### HTML Version - Edit Config in File

Buka file `erdgen-chen-improved-v2.html` di text editor, cari section `CONFIG`:

```javascript
const CONFIG = {
    layout: {
        paddingX: 250,
        paddingY: 200,
        colWidth: 800,
        entityWidth: 180,
        entityHeight: 50,
        attrLeftX: -260,
        attrRightX: 260,
        attrHeight: 28,
        attrWidth: 140,
        attrSpacing: 42,
        relationshipWidth: 110,
        relationshipHeight: 65,
        relationshipOffsetY: -20,
    },
    dynamicHeight: {
        base: 50,
        attrSpacing: 42,
        bottomPadding: 250,
        topPadding: 100,
        minLayerHeight: 500,
    },
    skipColumns: new Set([
        'created_at', 'updated_at', 'deleted_at', 
        'remember_token', 'email_verified_at'
    ]),
    maxTablesPerLayer: 3,
};
```

---

## 📖 Workflow Sehari-hari

### Workflow 1: Export dari MySQL
```bash
# Export database
mysqldump -u root -p my_database > my_database.sql

# Python version
cd dist
python3 erd_generator_improved.py

# HTML version
# 1. Buka erdgen-chen-improved-v2.html di browser
# 2. Drag & drop my_database.sql
# 3. Download result
```

### Workflow 2: Quick Test
```bash
# Buat test file
echo "CREATE TABLE users (id INT PRIMARY KEY) ENGINE=InnoDB;" > test.sql

# Python
python3 erd_generator_improved.py

# HTML
# Drag test.sql ke browser
```

### Workflow 3: Multiple Databases
```bash
# Generate untuk beberapa database
python3 erd_generator_improved.py
# Input: db1.sql → Output: erd-db1.drawio

python3 erd_generator_improved.py
# Input: db2.sql → Output: erd-db2.drawio
```

### Workflow 4: Team Collaboration
```bash
# 1. Share database.py untuk consistent config
git add dist/database.py
git commit -m "Update ERD config"
git push

# 2. Team members pull & generate
git pull
cd dist
python3 erd_generator_improved.py
```

---

## 🎨 Output Preview

### What You'll Get

**Entities:**
- Rectangle boxes dengan nama table
- Border tebal (strokeWidth: 2)
- Clean typography

**Attributes:**
- Ellipse shapes di kiri & kanan entity
- Zigzag/alternating placement
- Primary key: **Bold + Underline** + thick border
- Regular attributes: Normal style
- Connected dengan garis ke entity

**Relationships:**
- Diamond shapes dengan label "memiliki"
- Positioned di tengah antara entities
- Connected dengan garis dari entities

**Cardinality:**
- **N side**: Garis dengan **panah** (▶)
- **1 side**: Garis **tanpa panah**
- Labels "N", "M", "1" di sebelah garis

**Layout:**
- Hierarchical layers (top-down)
- No overlapping entities
- Balanced distribution
- Dynamic spacing based on content

---

## 🐛 Troubleshooting

### Python Version Issues

#### Error: "database.py tidak ditemukan!"
```bash
# Pastikan Anda di folder dist/
cd dist
ls  # harus ada database.py dan erd_generator_improved.py
```

#### Error: "ModuleNotFoundError: No module named 'lxml'"
```bash
# Install dependencies
pip3 install -r requirements.txt

# Atau manual
pip3 install lxml --break-system-packages
```

#### Error: "Tidak ada file SQL di folder ini!"
```bash
# Copy SQL file ke folder dist
cp /path/to/database.sql dist/
cd dist
python3 erd_generator_improved.py
```

### HTML Version Issues

#### File tidak ter-upload
- ✅ Pastikan file berekstensi `.sql`
- ✅ Check file size (max ~10MB untuk browser)
- ✅ Try different browser (Chrome recommended)

#### Diagram tidak generate
- ✅ Check browser console (F12) untuk errors
- ✅ Pastikan SQL format adalah MySQL/MariaDB
- ✅ Try with simple SQL file first

#### Download tidak working
- ✅ Check browser download settings
- ✅ Allow popups for the page
- ✅ Try right-click → Save As

### Layout Issues

#### Entities masih overlap
**Python - Edit `database.py`:**
```python
LAYOUT = {
    "col_width": 1000,  # Perbesar dari 800
    "padding_x": 300,   # Perbesar padding
}
```

**HTML - Edit config:**
```javascript
colWidth: 1000,
paddingX: 300,
```

#### Attributes terlalu rapat
```python
# Python - database.py
LAYOUT = {
    "attr_spacing": 50,  # Dari 42 → 50
}

# HTML
attrSpacing: 50,
```

#### Diagram terlalu besar/kecil
```python
# Adjust entity size
LAYOUT = {
    "entity_width": 150,   # Smaller
    "entity_height": 40,   # Smaller
}
```

---

## ❓ FAQ

### General

**Q: Perbedaan Python vs HTML version?**

| Feature | Python | HTML |
|---------|--------|------|
| Installation | ✅ Perlu install | ❌ Tidak perlu |
| Dependencies | lxml | ❌ None |
| Customization | ✅✅ Sangat fleksibel | ✅ Basic |
| File Selection | ✅ Interactive CLI | ✅ Drag & drop |
| Batch Processing | ✅ Via script | ❌ Manual |
| Best For | Development workflow | Quick demo/one-time |

**A:** Python untuk workflow rutin, HTML untuk quick test atau demo.

---

**Q: Apakah support PostgreSQL/Oracle?**

**A:** Saat ini hanya MySQL/MariaDB. Untuk database lain, export/convert ke MySQL format dulu.

---

**Q: Bisakah customize warna per entity?**

**A:** Warna berlaku global. Untuk per-entity, edit manual di draw.io setelah generate.

---

**Q: Kenapa foreign key tidak muncul sebagai attribute?**

**A:** Foreign key ditampilkan sebagai **relationship diamond**, sesuai Chen's ER Model.

---

**Q: Apakah junction table di-skip?**

**A:** Ya, junction table otomatis terdeteksi dan ditampilkan sebagai M:N relationship.

---

**Q: Diagram bisa export ke PNG/PDF?**

**A:** 
1. Buka file `.drawio` di https://app.diagrams.net
2. **File → Export as → PNG/JPEG/PDF/SVG**

---

**Q: License & commercial use?**

**A:** MIT License - 100% gratis, boleh untuk personal & commercial use.

---

**Q: Cara contribute?**

**A:**
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push & create Pull Request
5. Jangan lupa ⭐ star repository!

---

### Technical

**Q: Maximum file size?**

**A:**
- Python: No limit (depends on RAM)
- HTML: ~10MB (browser limitation)

---

**Q: Supported SQL features?**

**A:**
- ✅ CREATE TABLE
- ✅ PRIMARY KEY
- ✅ FOREIGN KEY
- ✅ ENGINE (InnoDB, MyISAM)
- ❌ VIEWs (ignored)
- ❌ TRIGGERs (ignored)
- ❌ STORED PROCEDUREs (ignored)

---

**Q: Composite primary key?**

**A:** Saat ini hanya support single-column primary key.

---

**Q: Running on server without GUI?**

**A:** Python version bisa dijalankan di terminal/SSH. HTML version perlu browser.

---

## 📚 Algorithm Details

### Improved Layering Algorithm

```
1. Parse SQL → Extract tables, columns, keys
2. Build dependency graph
3. Topological sorting → Order by dependencies
4. Layer balancing → Max 3-4 tables per layer
5. Collision detection → Calculate entity bounds
6. Position adjustment → Move if collision detected
7. Dynamic spacing → Based on attribute count
8. Generate XML → Create mxGraph structure
```

### Collision Detection

```javascript
function checkCollision(bounds, occupiedSpaces) {
    // Check horizontal overlap
    horizontalOverlap = (bounds.left < occupied.right && 
                        bounds.right > occupied.left)
    
    // Check vertical overlap
    verticalOverlap = (bounds.top < occupied.bottom && 
                       bounds.bottom > occupied.top)
    
    return horizontalOverlap && verticalOverlap
}
```

### Attribute Placement - Alternating/Zigzag

```
Entity: USER
├─ Left Side (even index):
│  ├─ id (PK) [0]
│  ├─ email [2]
│  └─ age [4]
└─ Right Side (odd index):
   ├─ name [1]
   ├─ password [3]
   └─ phone [5]
```

---

## 🎓 Best Practices

### ✅ DO

- ✅ Test dengan file SQL kecil dulu
- ✅ Backup file SQL sebelum generate
- ✅ Edit **hanya** `database.py` untuk Python version
- ✅ Commit config ke Git untuk team consistency
- ✅ Gunakan interactive mode untuk quick testing
- ✅ Adjust config jika diagram terlalu padat/renggang
- ✅ Review hasil di draw.io dan adjust manual jika perlu

### ❌ DON'T

- ❌ Jangan edit `erd_generator_improved.py` manual
- ❌ Jangan skip primary keys di `SKIP_COLUMNS`
- ❌ Jangan expect 100% perfect tanpa manual touch-up
- ❌ Jangan gunakan nama file dengan spasi/special chars
- ❌ Jangan delete `database.py` (mandatory)

---

## 💡 Tips & Tricks

### 1. Multiple Theme Versions
```python
# database.py - Theme 1: Light
COLORS = {"border": "#000000", "fill": "#ffffff", "line": "#000000"}
# Generate → output: erd-light.drawio

# database.py - Theme 2: Dark
COLORS = {"border": "#ECF0F1", "fill": "#2C3E50", "line": "#BDC3C7"}
# Generate → output: erd-dark.drawio
```

### 2. Quick Config Test
```bash
# Test config dengan small SQL
echo "CREATE TABLE test (id INT PRIMARY KEY) ENGINE=InnoDB;" > test.sql
python3 erd_generator_improved.py
```

### 3. Compare Layouts
```bash
# Generate dengan berbagai col_width
# col_width: 600 → erd-compact.drawio
# col_width: 800 → erd-normal.drawio
# col_width: 1000 → erd-spacious.drawio
```

### 4. Auto-open (macOS)
```bash
# Generate & auto-open
python3 erd_generator_improved.py && open erd-*.drawio
```

---

## 🌟 Comparison: v1.0 vs v2.0

| Feature | v1.0 | v2.0 (Improved) |
|---------|------|-----------------|
| **Layout Algorithm** | Simple grid | Topological + balancing |
| **Collision Detection** | ❌ | ✅ |
| **Attribute Placement** | Left-first | Alternating zigzag |
| **Arrows** | ❌ | ✅ N side |
| **Layer Balancing** | ❌ | ✅ Max 3-4/layer |
| **Spacing** | Fixed | Dynamic |
| **Canvas Size** | Fixed | Auto-adjust |
| **Primary Key Style** | Bold | Bold + Underline |

---

## 📄 License

MIT License

Copyright (c) 2026 Andy Pratama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 🆘 Support

Jika menemui masalah atau butuh bantuan:

1. ✅ Cek [Troubleshooting](#-troubleshooting)
2. ✅ Cek [FAQ](#-faq)
3. ✅ Create issue di [GitHub Issues](https://github.com/andypratama3/erd-generator-chen-notation/issues)
4. ✅ Email: **andypratama1211@gmail.com**

---

## ☕ Buy Me a Coffee

Jika project ini membantu Anda, dukung development dengan:

**[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/andypratama3)**

Atau scan QR:

```
https://buymeacoffee.com/andypratama3
```

**Terima kasih atas dukungannya!** ☕❤️

---

## 🙏 Acknowledgments

- **draw.io / diagrams.net** - Amazing diagramming platform
- **lxml** - Powerful XML processing library
- **Python Community** - For the ecosystem
- **All Contributors** - Thank you! 🙌
- **Coffee Supporters** - You fuel this project! ☕

---

## 📞 Contact & Links

- 🌐 **Website**: [andypratama.vercel.app](https://andypratama.vercel.app)
- 💻 **GitHub**: [@andypratama3](https://github.com/andypratama3)
- 📧 **Email**: andypratama1211@gmail.com
- ☕ **Buy Me a Coffee**: [buymeacoffee.com/andypratama3](https://buymeacoffee.com/andypratama3)

---

## 🔄 Changelog

### v2.0.0 (2026-01-29) - IMPROVED LAYOUT 🎉
- ✨ **NEW**: HTML standalone version
- ✨ **NEW**: Improved layering algorithm
- ✨ **NEW**: Collision detection & auto-adjustment
- ✨ **NEW**: Arrow indicators for cardinality
- ✨ **NEW**: Alternating/zigzag attribute placement
- ✨ **NEW**: Layer balancing (max 3-4 per layer)
- ✨ **NEW**: Dynamic spacing based on content
- ✨ **NEW**: Auto-centering for sparse layers
- ✨ **NEW**: Primary key with bold + underline
- ✨ **NEW**: Canvas size auto-adjustment
- 🔧 Improved: Better relationship positioning
- 🔧 Improved: Optimized entity spacing
- 🔧 Improved: Configuration options
- 📝 Updated: Comprehensive documentation

### v1.0.0 (2024-01-XX)
- ✨ Initial release
- ✅ Chen notation support
- ✅ 1:N and M:N relationships
- ✅ Interactive mode
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ Customizable via database.py

---

## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=andypratama3/erd-generator-chen-notation&type=Date)](https://star-history.com/#andypratama3/erd-generator-chen-notation&Date)

---

**Made with ❤️ and lots of ☕ for Database Designers**

**[⬆ Back to Top](#erd-generator---chen-notation)**