

import sqlite3




def halaman_buku():
    print("\n\n=== Halaman Buku ===")
    username = input("Masukan Username:")
    password = input("Masukan Password:")
        
    conn=sqlite3.connect("Admin_Database.db")
    cursor=conn.cursor()
        
    cursor.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (username,password) )
    user = cursor.fetchone()
    conn.close()