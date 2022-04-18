import sqlite3
def delete_data(id):
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor()
    c.execute("DELETE FROM address_book WHERE id=?", (id,))
    conn.commit()
    conn.close()
    print("Data deleted.")
    
id = input("Enter the id of the person you want to delete: ")
delete_data(id)