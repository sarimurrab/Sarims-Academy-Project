import sqlite3


def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id integer primary key , Name text, College text, Address text, Phone integer, Room integer, Payment text)")
    conn.commit()
    conn.close()


def insert(Name, College, Address, Phone, Room, Payment):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)",
                (Name, College, Address, Phone, Room, Payment))
    conn.commit()
    conn.close()


#insert("Sarim", "Mait", "Siyana", 123, 23, "Paid")


def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("select * from routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    # comma to delete after id all the value
    cur.execute("delete from routine where id=?", (id,))
    conn.commit()
    conn.close()


def search(Name='', College='', Address='', Phone='', Room='', Payment=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("select * from routine where Name =? OR College=? OR Address=? OR Phone=? OR Room=? OR Payment=?",
                (Name, College, Address, Phone, Room, Payment))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


connect()
