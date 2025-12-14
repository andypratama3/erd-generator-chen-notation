# 📊 ERD Generator - Chen Notation

Aplikasi Python untuk **membuat Entity-Relationship Diagram (ERD)** dalam format **draw.io** dari file SQL database Anda secara **otomatis & cepat**.

Menggunakan **Chen's ER Model** dengan:
- 🏢 Entity (Rectangle)
- 📝 Attribute (Ellipse)
- 💎 Relationship (Diamond)
- 🔗 Cardinality (1/M)

---

## ✨ Fitur Utama

✅ **Parse SQL Otomatis** - Baca file SQL dan ekstrak struktur database  
✅ **Generate ERD Chen** - Buat diagram dengan model Chen yang rapi  
✅ **Support Semua Relasi** - Handle 1:N, M:N, dan self-referencing relationships  
✅ **Cardinality Labels** - Tampilkan M & 1 secara otomatis  
✅ **Dynamic Layout** - Spacing otomatis berdasarkan jumlah attribute  
✅ **Draw.io Format** - Output langsung buka di draw.io, no conversion needed  
✅ **Customizable** - Edit warna, ukuran, spacing sesuai kebutuhan  
✅ **Zero Dependencies** - Hanya butuh `lxml` (lightweight)

---

## 🚀 Quick Start (5 Menit)

### 1. Clone Repository
```bash
git clone https://github.com/andypratama3/erd-generator-chen-notation.git
cd erd-generator-chen-notation/dist
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Hanya butuh 1 library:
- `lxml==4.9.3` (untuk generate XML)

### 3. Siapkan SQL File
```bash
# Gunakan contoh yang sudah ada:
# - database-example.sql (simple 5 tables)
# - database-ansor.sql (complex 25+ tables)

# Atau buat SQL file sendiri:
# 1. Export database Anda:
mysqldump -u username -p database_name > my-database.sql

# 2. Copy ke folder dist/
cp my-database.sql dist/
```

### 4. Update Konfigurasi (database.py)
```python
# Edit dist/database.py

# Ubah nama SQL file
SQL_FILE = "database-example.sql"  # atau "my-database.sql"

# Ubah nama output
OUTPUT_FILE = "MY_ERD.drawio"

# Ubah judul diagram
DIAGRAM_NAME = "My Database ERD"
```

### 5. Jalankan Script
```bash
python generate-erd.py
```

Output akan menampilkan:
```
📖 Membaca file SQL...
🔍 Parsing database...
📊 Menghitung attribute per tabel...
📈 Menghitung layer layout...
🎨 Membuat mxGraph XML...
🏢 Membuat entitas...
💎 Membuat relasi 1:N...
🔗 Membuat relasi M:N...
💾 Menyimpan file...
======================================================================
✅ ERD CHEN SESUAI GAMBAR BERHASIL DIBUAT!
======================================================================
📊 Total Tabel         : 5
🔗 Total Relasi        : 6
📈 Jumlah Layer        : 2
💾 File Output         : MY_ERD.drawio
======================================================================
```

### 6. Buka di Draw.io
```bash
# Opsi 1: Online (recommended)
1. Buka https://app.diagrams.net
2. File → Open → Pilih file .drawio yang baru dibuat
3. Diagram langsung muncul, bisa di-edit!

# Opsi 2: Desktop
1. Download draw.io desktop: https://github.com/jgraph/drawio-desktop
2. Double-click file .drawio
3. Edit & export sesuai kebutuhan
```

**Done!** Diagram ERD Anda siap! 🎉

---

## 📋 Project Structure

```
erd-generator-chen-notation/
│
├── README.md                    (File ini - Main documentation)
│
└── dist/                        (Working directory)
    ├── README.md                (Detailed documentation)
    ├── SETUP_GUIDE.md           (Detailed setup guide)
    ├── DATABASE_EXAMPLE.md      (Contoh database 5 tables)
    │
    ├── database.py              (Configuration - user edit)
    ├── generate-erd.py          (Main script - don't edit)
    ├── requirements.txt         (Dependencies)
    │
    ├── database-example.sql     (Simple example: 5 tables)
    ├── database-ansor.sql       (Complex example: 25+ tables)
    │
    └── .gitignore               (Git config)
```

---

## 🎯 Penggunaan Sehari-hari

### Use Case 1: Database Baru
```bash
# 1. Export database
mysqldump -u root -p my_database > my_database.sql

# 2. Copy ke folder
cp my_database.sql dist/

# 3. Edit database.py
nano dist/database.py
# Ubah: SQL_FILE = "my_database.sql"

# 4. Generate ERD
cd dist
python generate-erd.py

# 5. Buka MY_ERD.drawio di draw.io
```

### Use Case 2: Customize Style
```python
# Edit dist/database.py

# Ubah warna
COLORS = {
    "border": "#FF0000",   # Merah
    "fill": "#FFFF00",     # Kuning
    "line": "#0000FF",     # Biru
}

# Ubah spacing
LAYOUT = {
    "col_width": 700,      # Jarak antar table lebih jauh
    "padding_x": 200,
    "padding_y": 200,
}

# Run again
python generate-erd.py
```

### Use Case 3: Skip Kolom Tertentu
```python
# Edit dist/database.py

# Tambah kolom yang ingin di-skip
SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
    'remember_token',
    'email_verified_at',
    'your_custom_column',  # Tambah di sini
}

# Run again
python generate-erd.py
```

---

## 📊 Contoh Database

### Database Sederhana (5 Tables)
File: `database-example.sql`

```
Sistem Manajemen Karyawan & Proyek dengan relasi:
- DEPARTMENTS (Master)
- POSITIONS (Master)
- EMPLOYEES (FK → DEPARTMENTS, POSITIONS)
- PROJECTS (FK → DEPARTMENTS)
- PROJECT_ASSIGNMENTS (M:N Junction)
```

Jalankan:
```bash
python generate-erd.py
# Output: ANSOR_ERD_CHEN_FINAL.drawio
```

### Database Kompleks (25+ Tables)
File: `database-ansor.sql`

```
Sistem Organisasi ANSOR dengan relasi kompleks:
- Struktur organisasi (hierarki)
- Manajemen anggota & kepemimpinan
- Program pelatihan & sertifikasi
- Riwayat pendidikan, pekerjaan, skill
- Manajemen kegiatan & partisipasi
```

---

## 🔧 Konfigurasi Detail

### database.py - Configuration File

```python
# 1. SQL FILE
SQL_FILE = "database-example.sql"  # Ganti dengan nama file Anda

# 2. OUTPUT FILE
OUTPUT_FILE = "MY_ERD.drawio"      # Nama output diagram

# 3. DIAGRAM NAME
DIAGRAM_NAME = "My Database"       # Judul diagram

# 4. STYLING
COLORS = {
    "border": "#000000",  # Warna border (hitam)
    "fill": "#ffffff",    # Warna fill (putih)
    "line": "#000000",    # Warna garis (hitam)
}

# 5. LAYOUT
LAYOUT = {
    "padding_x": 150,           # Padding horizontal
    "padding_y": 150,           # Padding vertical
    "col_width": 500,           # Jarak antar table
    "entity_width": 160,        # Lebar entity box
    "entity_height": 45,        # Tinggi entity box
    "attr_spacing": 32,         # Jarak antar attribute
    "attr_per_side": 12,        # Max attribute per sisi
}

# 6. SKIP COLUMNS
SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
    'remember_token',
    'email_verified_at',
}
```

---

## 🐛 Troubleshooting

### Error: "FileNotFoundError: database-example.sql"
```bash
# Solusi: Pastikan file ada di folder dist/
ls dist/

# Atau copy dari template
cp database-example.sql dist/
```

### Error: "ModuleNotFoundError: lxml"
```bash
# Solusi: Install dependencies
pip install -r requirements.txt

# Atau manual
pip install lxml==4.9.3
```

### Error: "Invalid SQL syntax"
```bash
# Pastikan format SQL adalah MySQL:
✅ Benar:
CREATE TABLE `users` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`)
);

❌ Salah (PostgreSQL/SQLite):
CREATE TABLE users (
  id SERIAL PRIMARY KEY
);
```

### Diagram terlalu rapat/jauh
```python
# Edit dist/database.py

# Jika terlalu rapat:
LAYOUT = {
    "col_width": 700,      # Naikkan dari 500
    "padding_x": 250,      # Naikkan dari 150
}

# Jika terlalu jauh:
LAYOUT = {
    "col_width": 300,      # Turunkan dari 500
    "padding_x": 80,       # Turunkan dari 150
}

# Run: python generate-erd.py
```

### Attribute menumpuk/tidak terlihat
```python
# Edit dist/database.py

# Kurangi attribute yang ditampilkan
SKIP_COLUMNS = {
    'created_at',
    'updated_at',
    'deleted_at',
    'your_column_1',
    'your_column_2',
}

# Run: python generate-erd.py
```

---

## 📚 Dokumentasi Lengkap

Untuk informasi lebih detail, buka:

1. **dist/README.md** - Dokumentasi teknis lengkap
2. **dist/SETUP_GUIDE.md** - Panduan setup & customization
3. **dist/DATABASE_EXAMPLE.md** - Penjelasan contoh database

---

## 🎨 Output Preview

### Diagram yang Dihasilkan

```
┌─────────────────┐
│  DEPARTMENTS    │
│  ─────────────  │
│  id (PK)        │
│  name           │
│  code           │
└────────┬────────┘
         │ 1:N
         ├─────────────────┐
         │                 │
    ┌────▼──────────┐  ┌───▼────────┐
    │   EMPLOYEES   │  │  PROJECTS  │
    │  ───────────  │  │ ──────────  │
    │  id (PK)      │  │  id (PK)   │
    │  name         │  │  name      │
    │  dept_id (FK) │  │  budget    │
    │  pos_id (FK)  │  └───┬────────┘
    └────┬──────────┘      │ 1:N
         │ M:N             │
         │ (via)           │
         └─────────────────┤
                           ▼
              ┌──────────────────────┐
              │ PROJECT_ASSIGNMENTS  │
              │  ──────────────────  │
              │  id (PK)             │
              │  employee_id (FK)    │
              │  project_id (FK)     │
              │  role                │
              └──────────────────────┘
```

Ketika dibuka di draw.io:
- ✅ Semua entity terlihat rapi
- ✅ Relationship diamond dengan label "memiliki"
- ✅ Cardinality (M & 1) di garis relasi
- ✅ Attribute teorganisir per entity
- ✅ Layout hierarki otomatis
- ✅ Bisa di-edit & customize langsung di draw.io

---

## 💡 Tips & Tricks

### 1. Batch Process Multiple Databases
```bash
# Process multiple databases
for db in db1.sql db2.sql db3.sql; do
    cp $db dist/
    sed -i "s/SQL_FILE = .*/SQL_FILE = \"$db\"/" dist/database.py
    cd dist && python generate-erd.py && cd ..
done
```

### 2. Auto-Open di Draw.io
```bash
# macOS
open "https://app.diagrams.net/?title=$(basename $OUTPUT_FILE)&url=$(pwd)/$OUTPUT_FILE"

# Atau langsung buka file lokal dengan draw.io desktop
```

### 3. Export ke Format Lain
Di draw.io, bisa export ke:
- PNG/JPG - untuk presentasi
- SVG - untuk web
- PDF - untuk dokumentasi

### 4. Version Control
```bash
# Track database diagrams
git add dist/MY_ERD.drawio

# Bisa lihat history perubahan database
git log --oneline dist/MY_ERD.drawio
```

---

## 🤝 Contributing

Contributions welcome! Jika ada improvement:

1. Fork repository
2. Create feature branch
3. Test dengan database berbeda
4. Submit pull request

---

## 📄 License

MIT License - Bebas digunakan & modify

---

## 🆘 Support & Issues

Jika ada pertanyaan atau issue:

1. Baca file ini terlebih dahulu
2. Cek [dist/README.md](dist/README.md)
3. Cek [dist/SETUP_GUIDE.md](dist/SETUP_GUIDE.md)
4. Open issue di GitHub

---

## 🎉 Ready to Go!

```bash
# Siap?
cd dist
python generate-erd.py
```

Hasilnya akan membuat file `.drawio` yang bisa langsung dibuka di draw.io.

**Happy ERD Generation!** 📊✨

---

**Made with ❤️ untuk membuat dokumentasi database lebih mudah**