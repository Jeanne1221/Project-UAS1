from Halaman_Login import login
import sqlite3

def Buat_Database():
    conn=sqlite3.connect("Admin_Database.db")
    cursor=conn.cursor()
    
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL)
        '''
        )

    cursor.execute("SELECT * FROM admin WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ("Marsha", "Ajat123"))
    conn.commit()
    conn.close()
    
    

login()