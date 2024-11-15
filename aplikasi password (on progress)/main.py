import tkinter as tk
from tkinter import messagebox, Toplevel
import mysql.connector

# Fungsi untuk memeriksa login
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Membuat koneksi ke database MySQL
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",      # ganti sesuai user MySQL Anda
            password="root",  # ganti sesuai password MySQL Anda
            database="login_app"
        )
        cursor = conn.cursor()

        # Query untuk memeriksa username dan password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Sukses", "Selamat datang, Anda berhasil login!")
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

# Fungsi untuk membuka jendela registrasi
def open_register_window():
    register_window = Toplevel(root)
    register_window.title("Registrasi Pengguna Baru")
    
    # Label dan Entry untuk username
    tk.Label(register_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    entry_new_username = tk.Entry(register_window)
    entry_new_username.grid(row=0, column=1, padx=10, pady=10)

    # Label dan Entry untuk password
    tk.Label(register_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.grid(row=1, column=1, padx=10, pady=10)

    # Tombol untuk submit registrasi
    register_button = tk.Button(register_window, text="Register", 
                                command=lambda: register_user(entry_new_username.get(), entry_new_password.get()))
    register_button.grid(row=2, column=0, columnspan=2, pady=10)

# Fungsi untuk menambahkan user ke database
def register_user(username, password):
    # Membuat koneksi ke database MySQL
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",      # ganti sesuai user MySQL Anda
            password="root",  # ganti sesuai password MySQL Anda
            database="login_app"
        )
        cursor = conn.cursor()

        # Query untuk menambahkan user baru
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()

        messagebox.showinfo("Registrasi Sukses", "Pengguna berhasil ditambahkan!")
        
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Login dengan MySQL")

# Label dan Entry untuk username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Tombol Login
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=5)

# Tombol Register untuk membuka form registrasi
register_button = tk.Button(root, text="Register", command=open_register_window)
register_button.grid(row=3, column=0, columnspan=2, pady=5)

# Menjalankan aplikasi
root.mainloop()
