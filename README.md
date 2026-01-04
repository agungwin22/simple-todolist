# 📝 To-Do List - Python

Aplikasi **To-Do List** sederhana berbasis teks (CLI) yang ditulis dalam bahasa Python. Program ini memungkinkan pengguna untuk menambah, melihat, menandai selesai, dan menghapus tugas dengan mudah.

---

## ✨ Fitur

- ✅ **Tambah Tugas** – Tambahkan tugas baru ke dalam daftar.
- 👁️ **Lihat Tugas** – Tampilkan semua tugas beserta status (selesai/belum).
- ✔️ **Tandai Selesai** – Ubah status tugas menjadi selesai (ditandai dengan ✅).
- 🗑️ **Hapus Tugas** – Hapus tugas dari daftar.
- 🧠 **Penanganan Error** – Program sudah dilengkapi validasi input untuk mencegah kesalahan.
- 🔁 **Menu Interaktif** – Menu berulang hingga pengguna memilih keluar.

---

## 🚀 Cara Menjalankan

1. Pastikan Python sudah terinstall di komputer Anda (versi 3.x disarankan).
2. Unduh atau salin kode `todo.py`.
3. Buka terminal/command prompt di folder tempat file disimpan.
4. Jalankan perintah:

```bash
python todo.py
```

5. Ikuti instruksi menu yang muncul.

---

## 📂 Struktur Program

- `tasks` – List untuk menyimpan semua tugas (setiap tugas berupa dictionary dengan `task` dan `done`).
- `show_menu()` – Menampilkan pilihan menu.
- `add_task()` – Menambahkan tugas baru.
- `view_task()` – Menampilkan semua tugas beserta status.
- `mark_done()` – Menandai tugas sebagai selesai.
- `delete_task()` – Menghapus tugas berdasarkan nomor.
- Loop utama (`while True`) – Menjaga program tetap berjalan sampai pengguna keluar.

---

## 🛠️ Teknologi

- **Bahasa**: Python 3
- **Tipe Program**: CLI (Command Line Interface)
- **Fungsi Built-in**: `input()`, `print()`, `enumerate()`, `append()`, `pop()`

---

## 📷 Pratinjau Program

```
--- To Do List ---
-- Author agungwin22 --
1. Add Task
2. View Task
3. Mark Task as Done
4. Delete Task
5. Exit
Choose an option:
```

---

## 👨‍💻 Author

Dibuat oleh **agungwin22** sebagai proyek latihan Python sederhana.

---

## 📄 Lisensi

Proyek ini terbuka untuk umum dan dapat dimodifikasi sesuai kebutuhan.
