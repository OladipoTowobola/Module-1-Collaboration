# 1. IMPORTING NECESSARY MODULES
# Flask: The core web framework.
# request: To handle incoming data (like JSON from a POST request).
# jsonify: To turn Python dictionaries into JSON responses for the user.
# SQLAlchemy: The ORM (Object Relational Mapper) that lets us use Python instead of raw SQL.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 2. APP INITIALIZATION & CONFIGURATION
app = Flask(__name__)

# Set the database location. 'sqlite:///books.db' creates a file in your project folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'

# Disable tracking overhead to improve performance.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link the SQLAlchemy instance to our Flask app.
db = SQLAlchemy(app)

# 3. DEFINING THE DATA MODEL:This class defines what a "Book" looks like in our database tables.
# BOOK MODEL
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for every book
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False) # type: ignore

# Helper method to convert the database object into a dictionary.Essential for returning JSON data.
def to_dict(self):
    return {
        "id": self.id,
        "book_name": self.book_name,
        "author": self.author,
        "publisher": self.publisher
    }

# 4. DATABASE CREATION: with app.app_context() ensures the app is active when we trigger database creation.
# Create DB

with app.app_context():
    db.create_all()

# 5. CREATE: ADD A NEW BOOK

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json() # Extract JSON data from the request body
    new_book = Book(
       book_name=data['book_name'],
       author=data['author'],
       publisher=data['publisher']
       )
    db.session.add(new_book) #Add the book to the staging area
    db.session.commit()      #Save changes to the database
    return jsonify(new_book.to_dict()), 201   #Return the new book and a 201 "Created" Status

# 6. READ ALL: FETCH ALL BOOKS

@app.route('/books', methods=['GET'])
def get_book():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# 7. READ ONE: FETCH BY ID
    @app.route('/books/<int:id>' , methods=['GET'])
    def get_book(id):
        books = Book.query.get_or_404(id)
        return jsonify(book.to_dict())
    

# 8. UPDATE: MODIFY AN EXISTING BOOK
@app.route('/books/<int:id>' , methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    # .get() allows us to update only the fields provided, keeping old values as defaults. 

    book.book_name = data.get('book_name', book.book_name) 
    book.author    = data.get('author', book.author)        
    book.publisher = data.get('publisher', book.publisher)  
    # Save the updates to the database
    db.session.commit()  
    return jsonify({"message": "Book updated successfully"})
 


# 9. DELETE: REMOVE A BOOK
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)  # Mark the record for deletion
    db.session.commit()      # Execute the deletion
    return jsonify({"message": "Book deleted"})

# 10. RUN THE SERVER
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you save changes.
    app.run(debug=True)
    