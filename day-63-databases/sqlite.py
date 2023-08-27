import sqlite3

#creates a connection to a new database (if the database does not exist then it will be created).
db = sqlite3.connect("books-collection.db")

#creates a cursor which will control our database.
cursor = db.cursor()

#creates a new table in the database called book with 4 columns
cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE, "
               "author varchar(250) NOT NULL, "
               "rating FLOAT NOT NULL)")

#adds data to our table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")

#commit the changes to our database.
db.commit()

