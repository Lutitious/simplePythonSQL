#!/usr/bin/env python3
import sqlite3

def store_data(name, birthday, number, address,id):
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS address_book (name TEXT, birthday DATE, number TEXT, address TEXT, id INTEGER PRIMARY KEY)")
    c.execute("INSERT INTO address_book VALUES (?,?,?,?,?)", (name, birthday, number, address, id))
    conn.commit()
    conn.close()

name=input("Enter your name: ")
birthday=input("Enter your birthday (YYYY/MM/DD) : ")
number=input("Enter your phone number: ")
address=input("Enter your address: ")
id=input("Enter your id: ")
store_data(name, birthday, number, address, id)
print("Data stored.")

