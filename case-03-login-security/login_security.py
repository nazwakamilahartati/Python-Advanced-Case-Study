import re
import datetime
from functools import wraps

class User:
    """Menyimpan dan memvalidasi data pengguna."""

    def __init__(self, username, password):
        """Menginisialisasi username dan password."""
        self.username = username
        self.password = password

    @property
    def username(self):
        """Mengembalikan username pengguna."""
        return self._username

    @username.setter
    def username(self, value):
        """Memvalidasi format username."""
        if not re.fullmatch(r"[a-zA-Z0-9]{5,}", value):
            raise ValueError("Format username tidak valid")
        self._username = value

    @property
    def password(self):
        """Mengembalikan password pengguna."""
        return self._password

    @password.setter
    def password(self, value):
        """Memvalidasi panjang password dan keberadaan angka."""
        if len(value) < 8:
            raise ValueError("Password kurang dari 8 karakter")

        if not re.search(r"\d", value):
            raise ValueError("Password harus mengandung angka")

        self._password = value

def audit_log(func):
    """Mencatat waktu dan hasil percobaan login."""

    @wraps(func)
    def wrapper(username, password, database_users):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            user = User(username, password)

            if (
                username in database_users
                and database_users[username] == user.password
            ):
                status = "BERHASIL"
                alasan = ""
                func(username, password, database_users)
            else:
                status = "DITOLAK"
                alasan = "Username atau password salah"

        except ValueError as error:
            status = "DITOLAK"
            alasan = str(error)

        print(f"Waktu   : {waktu}")
        print(f"Username: {username}")

        if status == "BERHASIL":
            print(f"Status  : {status}")
        else:
            print(f"Status  : {status} - {alasan}")

        return status == "BERHASIL"

    return wrapper

@audit_log
def login_system(username, password, database_users):
    """Memeriksa kecocokan data login pengguna."""
    return (
        username in database_users
        and database_users[username] == password
    )

def main():
    """Menjalankan empat skenario pengujian login."""

    database_users = {
        "admin123": "rahasia2026",
        "budiUtomo": "password789",
        "mahasiswa01": "aman12345"
    }

    print("SISTEM KEAMANAN AKUN DAN AUDIT LOG LOGIN")
    print("-" * 52)

    print("\nPengujian: Username tidak valid")
    login_system("andi!", "securePass1", database_users)

    print("\nPengujian: Password terlalu pendek")
    login_system("andi01", "abc123", database_users)

    print("\nPengujian: Password tanpa angka")
    login_system("sinta01", "passwordLama", database_users)

    print("\nPengujian: Login berhasil")
    login_system("mahasiswa01", "aman12345", database_users)

    print()

if __name__ == "__main__":
    main()