# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4. As in 16.6,
# select and print the title column from the book table in alphabetical order.

import sqlalchemy

# 1. Connect to the database file you created
engine = sqlalchemy.create_engine('sqlite:///book.db')

# 2. Connect and execute the alphabetical select query
with engine.connect() as connection:
    # We select 'book_name' and use 'ORDER BY' for alphabetical order
    query = sqlalchemy.text("SELECT book_name FROM book ORDER BY book_name ASC")
    result = connection.execute(query)
    
    print("Alphabetical Book Titles:")
    for row in result:
        print(f"- {row[0]}")