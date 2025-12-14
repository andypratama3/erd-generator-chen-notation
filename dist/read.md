# 📊 ERD Generator - Chen Model

Aplikasi untuk menghasilkan **Entity-Relationship Diagram (ERD)** dalam format **draw.io** (.drawio) dari file SQL database Anda secara otomatis.

## ✨ Fitur

- ✅ Parse SQL dan deteksi relasi otomatis
- ✅ Generate ERD dengan model Chen (entity, attribute, relationship)
- ✅ Support relasi 1:N dan M:N (junction tables)
- ✅ Cardinality labels (M & 1) otomatis
- ✅ Dynamic spacing berdasarkan jumlah attribute
- ✅ Hierarchical layout rapi (layer-based)
- ✅ Styling customizable (warna, ukuran, font)
- ✅ Output bisa dibuka langsung di draw.io

## 📋 Prerequisites

- Python 3.7+
- pip (Python package manager)

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/erd-generator.git
cd erd-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Siapkan File SQL
Letakkan file SQL Anda di root folder dengan nama:
```
database-ansor.sql
```

Atau ubah nama file di `database.py`:
```python
SQL_FILE = "your-database.sql"
```

### 4. Jalankan Script
```bash
python generate-erd.py
```

### 5. Output
File `.drawio` akan tercipta:
```
ANSOR_ERD_CHEN_FINAL.drawio
```

### 6. Buka di Draw.io
1. Buka [draw.io](https://app.diagrams.net)
2. File → Open → Pilih file `.drawio`
3. Edit dan customize sesuai kebutuhan

## 📁 Project Structure

```
erd-generator/
├── dist/
│   ├── README.md                 # Dokumentasi (file ini)
│   ├── requirements.txt          # Dependencies
│   ├── database.py              # Konfigurasi
│   ├── generate-erd.py          # Logic utama
│   ├── database-ansor.sql       # Contoh SQL
│   └── .gitignore               # File yang di-ignore
└── .git/
```

## ⚙️ Konfigurasi

Edit file `database.py` untuk customize:

### 1. Nama File SQL
```python
SQL_FILE = "database-ansor.sql"  # Ubah sesuai file Anda
```

### 2. Nama File Output
```python
OUTPUT_FILE = "ERD_DIAGRAM.drawio"
DIAGRAM_NAME = "My Database"
```

### 3. Warna & Styling
```python
COLORS = {
    "border": "#000000",  # Hitam
    "fill": "#ffffff",    # Putih
    "line": "#000000",    # Hitam
}
```

### 4. Layout Configuration
```python
LAYOUT = {
    "padding_x": 150,        # Padding horizontal
    "padding_y": 150,        # Padding vertical
    "col_width": 500,        # Jarak antar entity
    "attr_spacing": 32,      # Jarak antar attribute
}
```

### 5. Skip Columns
```python
SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
}
```

## 📖 Cara Kerja

### 1. **Parsing SQL**
Script membaca file SQL dan mengekstrak:
- Nama tabel
- Column/attribute
- Primary key
- Foreign key (relasi)

### 2. **Deteksi M:N**
Otomatis mendeteksi junction tables:
- Jika tabel punya 2+ FK
- Dan tidak ada attribute lain (hanya FK)
- → Dianggap sebagai table relasi M:N

### 3. **Hierarchical Layout**
Menggunakan topological sort untuk menempatkan tabel:
- Master table (tidak punya FK) → Layer 0
- Detail table (depend on master) → Layer 1+
- Jarak antar layer: dynamic berdasarkan attribute count

### 4. **Generate mxGraph XML**
Membuat XML untuk draw.io dengan:
- Entity: Rectangle boxes
- Attribute: Ellipse shapes
- Relationship: Diamond shapes
- Cardinality: M & 1 labels

### 5. **Save File**
Output disimpan dalam format `.drawio` (XML-based)

## 🎨 Styling Chen Model

### Entity
- Shape: Rectangle
- Border: 1px, hitam
- Rounded corners
- Font: Bold, 11pt

### Attribute
- Shape: Ellipse
- Border: 1px, hitam
- Primary Key: Border 1.5px, Bold
- Font: 7pt (regular), 8pt (PK)

### Relationship
- Shape: Diamond (Rhombus)
- Label: "memiliki"
- Border: 1px, hitam
- Font: 8pt

### Lines/Edges
- Curved line (smooth)
- Color: Hitam (#000000)
- Width: 1px
- Cardinality: M (many), 1 (one)

## 📊 Contoh Output

Untuk database dengan tabel:
```
┌─────────────┐
│   anggota   │──── M ──── memiliki ──── 1 ──── kepengurusan
└─────────────┘
     │
     └──── M ──── memiliki ──── 1 ──── kegiatan
```

## 🔧 Troubleshooting

### Error: "File not found: database-ansor.sql"
**Solusi**: Pastikan file SQL ada di folder yang sama dengan script
```bash
ls database-ansor.sql  # Check apakah file ada
```

### Error: "lxml is not installed"
**Solusi**: Install dependencies
```bash
pip install -r requirements.txt
```

### Diagram terlalu rapat
**Solusi**: Ubah di `database.py`:
```python
LAYOUT = {
    "col_width": 700,      # Tambah nilai
    "padding_x": 200,
    "padding_y": 200,
}
```

### Attribute terlalu banyak dan menumpuk
**Solusi**: Kurangi jumlah attribute yang ditampilkan:
```python
SKIP_COLUMNS = {
    'created_at', 'updated_at', 'deleted_at',
    'remember_token', 'email_verified_at',
    'your_column_name',  # Tambah kolom yang ingin di-skip
}
```

## 📝 Contoh SQL

Pastikan format SQL sesuai dengan standar MySQL:

```sql
CREATE TABLE `anggota` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_lengkap` varchar(150) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `kepengurusan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_anggota` int DEFAULT NULL,
  `id_jabatan` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_anggota` (`id_anggota`),
  KEY `id_jabatan` (`id_jabatan`),
  CONSTRAINT `fk_kepengurusan_anggota` 
    FOREIGN KEY (`id_anggota`) REFERENCES `anggota` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 🎯 Output Interpretation

File `.drawio` yang dihasilkan berisi:

1. **Entity Boxes** - Tabel dengan nama
2. **Ellipses** - Attribute/column
   - Dengan underline = Primary Key
3. **Diamonds** - Relationship dengan label "memiliki"
4. **Lines** - Connections dengan cardinality (M/1)

## 📚 Membuka di Draw.io

### Online
1. Buka https://app.diagrams.net
2. File → Open → Pilih `.drawio` file
3. Edit, customize, export

### Desktop (Recommended)
1. Download draw.io desktop: https://github.com/jgraph/drawio-desktop
2. Open file dengan drag & drop
3. Edit offline, save otomatis

## 🔗 Links

- [draw.io - Diagram Editor](https://app.diagrams.net)
- [Entity-Relationship Model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [lxml Documentation](https://lxml.de/)

## 📄 License

MIT License - Feel free to use and modify

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 💬 Support

Ada pertanyaan atau issue?
1. Check README ini terlebih dahulu
2. Baca troubleshooting section
3. Open issue di GitHub

## ✅ Checklist Sebelum Clone

- [ ] Python 3.7+ terinstall
- [ ] pip terinstall
- [ ] File SQL siap
- [ ] draw.io account (optional, bisa offline)

---

**Happy Diagramming!** 🎉

Dibuat dengan ❤️ untuk membuat dokumentasi database lebih mudah