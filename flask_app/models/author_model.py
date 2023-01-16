from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model



class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # many to many: this empty list is added to each
        self.books = []



# ? --------------------------------------
    # READ all authors, display on frontend
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("books_schema").query_db(query)

        authors = []

        for author in results:
            authors.append(cls(author))
        
        return authors
# ? --------------------------------------



# ? --------------------------------------
    # CREATE new dojos, add form data to database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(author)s, NOW(), NOW());"

        return connectToMySQL("books_schema").query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # READ one author, show on frontend
    # @classmethod
    # def get_one(cls, data):
    #     query  = "SELECT * FROM authors WHERE id = %(id)s;" 
    #     result = connectToMySQL('books_schema').query_db(query, data)

    #     return cls(result[0]) 
# ? --------------------------------------



# ? --------------------------------------
# ! I think the get_one() method used in the controller needs to be replaced with this one
    @classmethod
    def get_author_by_id(cls, data):
        query = """
        SELECT * FROM authors 
        LEFT JOIN favorites ON favorites.author_id = authors.id
        LEFT JOIN books ON favorites.book_id = books.id 
        WHERE authors.id = %(id)s;
        """

        results = connectToMySQL("books_schema").query_db(query, data)

        author = cls(results[0])

        for row in results:
            # this is book data
            # ! does it screw up the data param above if this is also called data? Change it here
            book_data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.books.append(book_model.Book(book_data))
            
        print(author)
        return author
# ? --------------------------------------



# ? --------------------------------------
    # ! what is this doing? Getting an author that doesn't have a book id? NO CLUE WHAT'S HAPPENING HERE !!!!!!!!!!!!!!!!!!!!!
    @classmethod
    def get_authors_not_favorited(cls, data):
        # ! NO IDEA WHAT'S HAPPENING IN THIS QUERY
        query = """
        SELECT * FROM authors 
        WHERE authors.id NOT IN 
        ( SELECT favorites.author_id FROM favorites WHERE favorites.book_id = %(id)s );
        """

        results = connectToMySQL('books_schema').query_db(query, data)

        authors = []

        # create a book object, add it to the books list on line 99 above
        for row in results:
            authors.append(cls(row))

        print(authors)
        return authors
# ? --------------------------------------



# ? --------------------------------------
    # ! Is this for a form on the view author page???? 
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query, data);
# ? --------------------------------------



# ? --------------------------------------
    # UPDATE dojos with form data
    # @classmethod
    # def update_one(cls, data):
    #     query  = "UPDATE dojos SET name = %(new_dojo)s, updated_at = NOW() WHERE id = %(id)s;" 

    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------



# ? --------------------------------------
    # DELETE dojos
    # ! How would you handle deleting a dojo if there were ninjas assigned to it?
    # @classmethod
    # def remove_one(cls, data):
    #     query = "DELETE FROM dojos WHERE id = %(id)s;"

    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
# ? --------------------------------------

