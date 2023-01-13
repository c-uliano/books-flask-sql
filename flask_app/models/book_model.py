from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']



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
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM books WHERE id = %(id)s;" 
        result = connectToMySQL('books_schema').query_db(query, data)

        return cls(result[0]) 
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

