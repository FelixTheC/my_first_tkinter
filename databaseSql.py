#! /usr/env/python3
import sqlite3

def dbConnect(dbname='lib.db'):
    conn = sqlite3.connect(dbname)
    return conn

def create_table(dbConnect, table, text):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS "+ table +" ("+ text +")")
    conn.commit()
    conn.close

def insert(dbConnect, table, value1, value2, value3, value4):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute('INSERT INTO ' + table + ' VALUES(NULL,?,?,?,?)',
     (value1, value2, value3, value4))
    conn.commit()
    conn.close

def update(dbConnect, table, id, title, author, year, isbn):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute("UPDATE "+ table +" SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

def delete(dbConnect, table, id):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute('DELETE FROM '+ table +' WHERE id=?', (id,))
    conn.commit()
    conn.close

def search(dbConnect, title="",author="",year="",isbn=""):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def view(dbConnect, table):
    conn = dbConnect
    cur = conn.cursor()
    cur.execute('SELECT * FROM '+ table)
    rows = cur.fetchall()
    conn.close
    return rows
