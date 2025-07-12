# Django TODO Application

![Django](https://img.shields.io/badge/Django-3.1.5-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Aplikasi TODO sederhana yang dibangun dengan Django framework. Aplikasi ini memungkinkan pengguna untuk membuat, mengelola, dan melacak tugas-tugas mereka dengan antarmuka yang bersih dan responsif.

## ✨ Fitur

- ✅ **Membuat Tugas Baru** - Tambahkan tugas dengan judul dan tanggal jatuh tempo
- ✏️ **Edit Tugas** - Perbarui informasi tugas yang sudah ada
- 🗑️ **Hapus Tugas** - Hapus tugas yang tidak diperlukan
- ☑️ **Tandai Selesai** - Tandai tugas sebagai selesai atau belum selesai
- 📅 **Tanggal Jatuh Tempo** - Atur dan pantau tanggal jatuh tempo tugas
- 📱 **Responsif** - Antarmuka yang kompatibel dengan berbagai perangkat
- 🎨 **UI Modern** - Desain yang bersih dengan Bootstrap styling

## 🛠️ Teknologi yang Digunakan

- **Backend**: Django 3.1.5
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4.3.1, jQuery
- **UI Components**: jQuery UI untuk date picker

## 📋 Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda memiliki:

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Git (untuk cloning repository)

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/django-todo-app.git
cd django-todo-app
```

### 2. Buat Virtual Environment

```bash
# Untuk Windows
python -m venv env
env\Scripts\activate

# Untuk macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install django==3.1.5
```

### 4. Konfigurasi Environment Variables

Buat file `.env` di root directory dan tambahkan:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
```

**Penting**: Jangan gunakan secret key default dalam production!

### 5. Migrasi Database

```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### 6. Buat Superuser (Opsional)

```bash
python manage.py createsuperuser
```

### 7. Jalankan Server

```bash
python manage.py runserver
```

Aplikasi akan berjalan di `http://127.0.0.1:8000/`

## 📁 Struktur Proyek

```
django-todo-app/
├── src/
│   ├── djangoproject/          # Konfigurasi utama Django
│   │   ├── __init__.py
│   │   ├── settings.py         # Pengaturan aplikasi
│   │   ├── urls.py            # URL routing utama
│   │   ├── wsgi.py            # WSGI configuration
│   │   └── asgi.py            # ASGI configuration
│   ├── todo/                   # Aplikasi TODO
│   │   ├── __init__.py
│   │   ├── admin.py           # Konfigurasi admin
│   │   ├── apps.py            # Konfigurasi aplikasi
│   │   ├── models.py          # Model database
│   │   ├── views.py           # View functions
│   │   ├── forms.py           # Form definitions
│   │   ├── tests.py           # Unit tests
│   │   ├── templates/         # Template HTML
│   │   │   ├── list_task.html
│   │   │   ├── update_task.html
│   │   │   └── delete_task.html
│   │   └── migrations/        # Database migrations
│   ├── manage.py              # Django management script
│   └── db.sqlite3            # Database file
├── env/                       # Virtual environment
├── bug_fixes_report.md       # Laporan perbaikan bug
├── .gitattributes
└── README.md
```

## 🎯 Penggunaan

### Membuat Tugas Baru

1. Buka aplikasi di browser
2. Isi field "Task title" dengan judul tugas
3. Isi field "Due date" dengan tanggal jatuh tempo (opsional)
4. Klik tombol "Save" untuk menyimpan tugas

### Mengelola Tugas

- **Update Tugas**: Klik tombol "Update" pada tugas yang ingin diubah
- **Hapus Tugas**: Klik tombol "Delete" pada tugas yang ingin dihapus
- **Tandai Selesai**: Gunakan checkbox dalam form update untuk menandai tugas sebagai selesai

### Tampilan Tugas

- Tugas diurutkan berdasarkan status penyelesaian dan tanggal jatuh tempo
- Tugas yang sudah selesai akan ditampilkan dengan garis coret
- Tugas yang belum selesai menampilkan countdown timer untuk tanggal jatuh tempo

## 🔧 Konfigurasi

### Database

Aplikasi menggunakan SQLite3 secara default. Untuk menggunakan database lain, ubah konfigurasi di `src/djangoproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Environment Variables

Aplikasi mendukung environment variables berikut:

- `DJANGO_SECRET_KEY`: Secret key untuk Django (wajib dalam production)
- `DEBUG`: Mode debug (True/False)
- `ALLOWED_HOSTS`: Daftar host yang diizinkan (untuk production)

## 🧪 Testing

Jalankan unit tests:

```bash
cd src
python manage.py test
```

## 📊 Model Data

### Task Model

```python
class task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
```

**Fields:**
- `title`: Judul tugas (maksimal 200 karakter)
- `complete`: Status penyelesaian tugas (True/False)
- `created`: Tanggal dan waktu pembuatan tugas
- `due`: Tanggal dan waktu jatuh tempo tugas (opsional)

## 🚀 Deployment

### Production Settings

Untuk deployment production, pastikan untuk:

1. **Set Environment Variables**:
   ```env
   DJANGO_SECRET_KEY=your-very-secure-secret-key
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```

3. **Use Production Database**:
   Ganti SQLite dengan PostgreSQL atau MySQL untuk production

4. **Configure Web Server**:
   Gunakan Nginx + Gunicorn atau Apache + mod_wsgi

### Docker Deployment

Buat `Dockerfile`:

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🔒 Keamanan

Aplikasi telah diperbaiki dari beberapa vulnerability:

- ✅ **Secret Key**: Tidak lagi hardcoded dalam kode
- ✅ **Input Validation**: Form validation untuk mencegah input yang tidak valid
- ✅ **Error Handling**: Proper 404 handling untuk resource yang tidak ditemukan
- ✅ **CSRF Protection**: Django CSRF protection aktif

## 🐛 Bug Fixes

Lihat [bug_fixes_report.md](bug_fixes_report.md) untuk detail lengkap tentang perbaikan bug yang telah dilakukan.

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Menampilkan daftar semua tugas |
| POST | `/` | Membuat tugas baru |
| GET | `/update_task/<id>/` | Menampilkan form update tugas |
| POST | `/update_task/<id>/` | Memperbarui tugas |
| GET | `/delete_task/<id>/` | Menampilkan konfirmasi hapus |
| POST | `/delete_task/<id>/` | Menghapus tugas |
| GET | `/admin/` | Admin interface |

## 🤝 Contributing

1. Fork repository
2. Buat branch feature (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push ke branch (`git push origin feature/amazing-feature`)
5. Buat Pull Request

## 📄 License

Project ini dilisensikan under MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 👨‍💻 Author

**Developer Name**
- Email: your.email@example.com
- GitHub: [@username](https://github.com/username)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap untuk UI components
- jQuery UI untuk date picker
- Komunitas Django Indonesia

## 📞 Support

Jika Anda mengalami masalah atau memiliki pertanyaan:

1. Buat issue di GitHub repository
2. Kirim email ke support@example.com
3. Join Discord server: [link-discord]

---

⭐ Jangan lupa untuk memberikan star pada repository ini jika bermanfaat!
