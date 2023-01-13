from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author_model

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
def create():
    author_model.Author.save(request.form)

    return redirect('/authors') 
# ? --------------------------------------



# ? --------------------------------------
# READ one dojo, show on frontend
# @app.route('/view/dojo/<int:id>') 
# def view_dojo(id):
#     data = { 
#         "id": id 
#     }

#     return render_template("show_dojo.html", dojo = Dojo.get_dojo_with_ninjas(data))  
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
