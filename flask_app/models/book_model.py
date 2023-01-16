from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # many to many: this empty list is added to each
        self.authors = []



# ? --------------------------------------
    # READ all ninjas, display on frontend
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL("books_schema").query_db(query)

        books = []

        for book in results:
            books.append(cls(book))
        
        return books
# ? --------------------------------------



# ? --------------------------------------
    # CREATE new ninjas, add form data to database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(number)s, NOW(), NOW());"

        return connectToMySQL("books_schema").query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # READ one book, show on frontend
    # @classmethod
    # def get_one(cls, data):
    #     query  = "SELECT * FROM books WHERE id = %(id)s;" 
    #     result = connectToMySQL('books_schema').query_db(query, data)

    #     return cls(result[0]) 
# ? --------------------------------------



# ? --------------------------------------
    # get a book by it's id
    @classmethod
    def get_book_by_id(cls, data):
        query = """
        SELECT * FROM books 
        LEFT JOIN favorites ON favorites.book_id = books.id 
        LEFT JOIN authors ON favorites.author_id = authors.id
        WHERE books.id = %(id)s;
        """

        results = connectToMySQL("books_schema").query_db(query, data)

        book = cls(results[0])

        for row in results:
            # this is author data
            # ! does it screw up the data param above if this is also called data? Change it here
            author_data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors.append(author_model.Author(author_data))
            
        print(book)
        return book
# ? --------------------------------------



# ? --------------------------------------
    # ! what is this doing? Getting a book that doesn't have an author id? NO CLUE WHAT'S HAPPENING HERE !!!!!!!!!!!!!!!!!!!!!
    @classmethod
    def get_books_not_favorited(cls, data):
        # ! NO IDEA WHAT'S HAPPENING IN THIS QUERY
        query = """
        SELECT * FROM books 
        WHERE books.id NOT IN 
        ( SELECT favorites.book_id FROM favorites WHERE favorites.author_id = %(id)s );
        """

        results = connectToMySQL('books_schema').query_db(query, data)

        books = []

        # create a book object, add it to the books list on line 99 above
        for row in results:
            books.append(cls(row))

        print(books)
        return books
# ? --------------------------------------



# ? --------------------------------------
    # UPDATE dojos with form data
    # @classmethod
    # def update_one(cls, data):
    #     query  = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;" 

    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # DELETE dojos
    # @classmethod
    # def remove_one(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s;"

    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------

