
markdown
Copy
Edit
# Hipoverse Task Auto

Script ini digunakan untuk menjalankan semua `daily task` di platform [Hipoverse](https://hipoverse.xyz/join?ref=927137319058829362) secara otomatis untuk banyak akun, serta menampilkan poin dari masing-masing akun setelah task dijalankan.

---

## 📁 Struktur File

- `akun.jsonl` — berisi token Bearer per baris (satu token per akun).
- `main.py` — script Python utama.

---

## 🧾 Contoh Format `akun.jsonl`

```text
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.aaa...
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.bbb...
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ccc...
🚀 Cara Menjalankan
Install Python 3.7+ (direkomendasikan: 3.10).

Install dependensi:

pip install requests
Jalankan script:
python main.py



⚙️ Fitur
✅ Menjalankan semua task harian (daily task) untuk tiap akun

✅ Menampilkan hasil response per task

✅ Menampilkan poin yang didapat per akun

✅ Otomatis membaca banyak akun dari akun.jsonl

✅ Ekstrak user_id dari token JWT secara lokal tanpa library tambahan

💡 Catatan
Token harus valid. Jika kadaluarsa (expired), task akan gagal.

user_id diambil otomatis dari token (sub dari payload JWT).

Script tidak menyimpan data pribadi, hanya memproses token dari file lokal.
