

import sqlite3



def login():
    print("\n\n=== LOGIN ===")
    username = input("Masukan Username:")
    password = input("Masukan Password:")
        
    conn=sqlite3.connect("Admin_Database.db")
    cursor=conn.cursor()
        
    cursor.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (username,password) )
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login Berhasil Anda Adalah Admin.")
        from Halaman_Buku import data
        data()
    else:
        print("Username/Password Salah!")
        return login()

