# Importing sqlite3 Module
import sqlite3

try:

   # Making a connection between sqlite3 database and Python Program
   conn = sqlite3.connect('db.sqlite3')

   # Creating cursor object using the connection object
   cursor = conn.cursor()

   # Excuting our sql query
   cursor.execute("select * from catalog_enquiry")

   # Printing rows
   rows = cursor.fetchall()
   for row in rows:
    print(row)
    
except sqlite3.Error as error:
    print("Failed to execute the above query", error)
    
finally:
   # Inside Finally Block, If connection is
    # open, we need to close it
    if conn:
        
        # using close() method, we will close 
        # the connection
        conn.close()
        
        # After closing connection object, we 
        # will print "the sqlite connection is 
        # closed"
        print("the sqlite connection is closed")  