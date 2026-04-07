# LSPP Python App

Aplikasi Python sederhana yang berisi 2 bagian utama:

- Bagian 1: SQLite numbers processing
- Bagian 2: Shape calculator (square, rectangle, circle)

## 1) Preparation / Requirements

### Software

- Python 3.9+ (disarankan Python 3.10 atau lebih baru)
- SQLite3 CLI (opsional, untuk inspeksi database manual)

### Cek Environment

```bash
python3 --version
sqlite3 --version
```

## 2) Project Specification

### Bagian 1: Numbers + SQLite

Fitur utama:

- Membuat / reset tabel numbers di database SQLite
- Menyimpan data angka dalam bahasa Indonesia menjadi angka integer
- Menghapus data ganjil
- Menampilkan data terurut dengan label:
  - genap
  - ganjil

Spesifikasi database:

- Lokasi file DB: db/numbers.db
- Tabel: numbers
- Kolom:
  - id: INTEGER PRIMARY KEY AUTOINCREMENT
  - angka: INTEGER NOT NULL

Catatan behavior saat run:

- Setiap run Bagian 1 akan drop dan create ulang tabel numbers
- Lalu seed data diinsert ulang
- Lalu data ganjil dihapus

### Bagian 2: Shape Calculator

Fitur utama:

- User memilih shape lewat input:
  - 1: square
  - 2: rectangle
  - 3: circle
- User memasukkan nilai dimensi sesuai shape
- Program menghitung:
  - Luas
  - Keliling
- Hasil ditampilkan ke terminal

## 3) Project Structure

```text
lspp-python/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── part1.py
│   ├── part2.py
│   └── models/
│       └── shape.py
├── db/
│   └── numbers.db
├── tests/
│   ├── test_part1.py
│   ├── test_part2.py
│   └── test_shape.py
└── README.md
```

## 4) How To Run / App Flow

### Menjalankan aplikasi utama

Dari root project:

```bash
python3 app/main.py
```

Flow di main:

1. Program meminta pilihan bagian:
   - 1 untuk Bagian 1
   - 2 untuk Bagian 2
2. Program menjalankan fungsi sesuai pilihan.

### Menjalankan Bagian 1 langsung

```bash
python3 app/part1.py
```

Output berupa tabel ASCII berisi id, angka, dan label genap/ganjil.

### Menjalankan Bagian 2 langsung

```bash
python3 app/part2.py
```

Contoh flow:

1. Pilih shape
2. Isi nilai dimensi
3. Lihat hasil luas dan keliling

## 5) Testing

Project menggunakan Python unittest.

Jalankan semua test:

```bash
python3 -m unittest discover -s tests -v
```

Cakupan test saat ini:

- part1 behavior dan integrasi SQLite
- part2 input handling dan perhitungan shape
- inisialisasi class di shape model

## 6) Notes

- Data label genap/ganjil di Bagian 1 dihitung saat display, tidak disimpan sebagai kolom di database.

### Author

- Name: I Nyoman Erik Aristayasa
- NIM: 230030329

