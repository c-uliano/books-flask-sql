from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import book_model, author_model



# ? --------------------------------------
# READ all books, display on frontend
@app.route('/books') 
def books():
    return render_template("books.html", books = book_model.Book.get_all())  
# ? --------------------------------------



# ? --------------------------------------
# CREATE new book, POST data
@app.route('/create/book', methods=['POST']) 
def create_book():
    book_model.Book.save(request.form)

    # return redirect(f"/view/dojo/{request.form['dojo_id']}") 
    return redirect("/books") 
# ? --------------------------------------



# ? --------------------------------------
# READ one book, show on frontend with associated authors
@app.route('/view/book/<int:id>') 
def view_book(id):
    data = { 
        "id": id 
    }

    return render_template("view_book.html", book = book_model.Book.get_book_by_id(data), authors = author_model.Author.get_authors_not_favorited(data))  
    # these are pulling the same id's, books, just from 2 different tables
# ? --------------------------------------



# ? --------------------------------------
# CREATE, POST data
@app.route('/create/book_fav', methods=['POST']) 
def create_book_fav():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }

    author_model.Author.add_favorite(data)
    return redirect(f"/view/book/{request.form['book_id']}") 
# ? --------------------------------------



# ? --------------------------------------
# Collectively this is to EDIT a dojo
# READ one ninja, show on frontend in filled-out form
# @app.route('/update/ninja/<int:id>') 
# def update_ninja(id):   
#     data = { 
#         "id": id 
#     }

#     return render_template("update_ninja.html", ninja = ninja.Ninja.get_one(data), dojos = dojo.Dojo.get_all())  

# UPDATE ninja, collect form data
# need hidden input on the form with the dojos id
# @app.route('/update/ninja', methods=['POST']) 
# def update_ninja_form():
#     ninja.Ninja.update_one(request.form)

#     return redirect(f"/view/dojo/request.form['dojo_id']")  
# ? --------------------------------------


# ? --------------------------------------
# DELETE ninja
# @app.route('/delete/ninja/<int:id>') 
# def delete_user(id):

#     data ={ 
#         "id": id
#     }

#     ninja.Ninja.remove_one(data)

#     return redirect("/")  
# ? --------------------------------------








