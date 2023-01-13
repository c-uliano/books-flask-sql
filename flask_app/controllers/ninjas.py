from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo, ninja



# ? --------------------------------------
# Add ninja form
@app.route('/ninjas') 
def ninja_form():
    return render_template("create_ninja.html", dojos = dojo.Dojo.get_all())  
# ? --------------------------------------



# ? --------------------------------------
# CREATE new ninja, POST data
@app.route('/create/ninja', methods=['POST']) 
def create_ninja():
    ninja.Ninja.save(request.form)

    
    return redirect(f"/view/dojo/{request.form['dojo_id']}") 
# ? --------------------------------------



# ? --------------------------------------
# Collectively this is to EDIT a dojo
# READ one ninja, show on frontend in filled-out form
@app.route('/update/ninja/<int:id>') 
def update_ninja(id):   
    data = { 
        "id": id 
    }

    return render_template("update_ninja.html", ninja = ninja.Ninja.get_one(data), dojos = dojo.Dojo.get_all())  

# UPDATE ninja, collect form data
# need hidden input on the form with the dojos id
@app.route('/update/ninja', methods=['POST']) 
def update_ninja_form():
    ninja.Ninja.update_one(request.form)

    return redirect(f"/view/dojo/request.form['dojo_id']")  
# ? --------------------------------------


# ? --------------------------------------
# DELETE ninja
@app.route('/delete/ninja/<int:id>') 
def delete_user(id):

    data ={ 
        "id": id
    }

    ninja.Ninja.remove_one(data)

    return redirect("/")  
# ? --------------------------------------



# ? --------------------------------------
# READ dojos, show on frontend
# @app.route('/view/dojo/<int:id>') 
# def view_user(id):
#     data = { 
#         "id": id 
#     }

#     return render_template("show_dojo.html", user = dojo.Dojo.get_one(data))  
# ? --------------------------------------




