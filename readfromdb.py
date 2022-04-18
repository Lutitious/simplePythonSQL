#!/usr/bin/env python3
import sqlite3
def retrieve_data(id):
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("SELECT * FROM address_book WHERE id=?", (id,))
    data=c.fetchall()
    conn.close()
    return data


id = input("Enter the id of the person you want to search: ")
data = retrieve_data(id)
if data == []:
    print("No data found.")
for i in data:
    print("Name:", i[0])
    print("Birthday:", i[1])
    print("Number:", i[2])
    print("Address:", i[3])