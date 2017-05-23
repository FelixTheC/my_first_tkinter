#! /usr/env/python3
import sqlite3

def dbConnect(dbname='lib.db'):
    conn = sqlite3.connect(dbname)
    return conn

def create_table():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close

def insert(item, quantity, price):
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES(?,?,?)', (item, quantity,price))
    conn.commit()
    conn.close

def update(quantity, price, item):
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))
    conn.commit()
    conn.close

def delete(item):
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=?', (item,))
    conn.commit()
    conn.close

def view():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close
    return rows
