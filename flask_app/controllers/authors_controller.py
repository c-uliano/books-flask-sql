from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author_model, book_model

# ? --------------------------------------
# Index page redirects to /dojos
@app.route('/') 
def index():
    return redirect("/authors")  
# ? --------------------------------------



# ? --------------------------------------
# READ all authors, display on frontend
@app.route('/authors') 
def all():
    return render_template("index.html", authors = author_model.Author.get_all())  
# ? --------------------------------------



# ? --------------------------------------
# CREATE new author, POST data
@app.route('/create/author', methods=['POST']) 
def create_author():
    author_model.Author.save(request.form)

    return redirect('/authors') 
# ? --------------------------------------



# ? --------------------------------------
# READ one author, show on frontend
@app.route('/view/author/<int:id>') 
def view_author(id):
    data = { 
        "id": id 
    }

    # this needs to pull the same id's, authors, from 2 different tables
    return render_template("view_author.html", author = author_model.Author.get_author_by_id(data), books = book_model.Book.get_books_not_favorited(data))  
# ? --------------------------------------



# ? --------------------------------------
# CREATE, POST data
@app.route('/create/author_fav', methods=['POST']) 
def create_author_fav():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }

    author_model.Author.add_favorite(data)
    return redirect(f"/view/book/{request.form['author_id']}") 
# ? --------------------------------------



# ? --------------------------------------
# Collectively this is to EDIT a dojo
# READ one dojos, show on frontend in filled-out form
# @app.route('/update/dojo/<int:id>') 
# def update_user(id):   
#     data = { 
#         "id": id 
#     }

#     return render_template("update_dojo.html", dojo = Dojo.get_one(data))  

# UPDATE dojos, collect form data
# need hidden input on the form with the dojos id
# @app.route('/update/dojo', methods=['POST']) 
# def update_user_form():
#     Dojo.update_one(request.form)

#     return redirect("/")  
# ? --------------------------------------



# ? --------------------------------------
# DELETE dojos
# @app.route('/delete/user/<int:id>') 
# def delete_user(id):

#     data ={ 
#         "id": id
#     }

#     Dojo.remove_one(data)

#     return redirect("/")  
# ? --------------------------------------
