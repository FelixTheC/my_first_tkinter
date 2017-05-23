#! /usr/env/python3
import psycopg2

def dbConnect():
    conn = psycopg2.connect("dbname='greslib.db' user='postgres' password='postgres123' host='localhost'")
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
    cur.execute('INSERT INTO store VALUES(%s, %s, %s)', (item, quantity,price))
    conn.commit()
    conn.close

def update(quantity, price, item):
    conn = psycopg2.connect('greslib.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))
    conn.commit()
    conn.close

def delete(item):
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    conn.commit()
    conn.close

def view():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close
    return rows
