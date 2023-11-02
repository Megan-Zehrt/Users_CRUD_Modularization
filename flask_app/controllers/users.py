from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

# Main Page
@app.route("/users")
def Read():
    all_users = User.get_all()
    return render_template("Read.html", all_users = all_users)

#Create User
@app.route("/users/new")
def new_user():
   return render_template("Create.html")

@app.route("/create_user", methods=['POST'])
def create_user():
   data = {
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'email': request.form['email']
   }
   id = User.create_one(data)
   return redirect(f'/users/show/{id}')

# Show User
@app.route("/users/show")
def user_show():
   return render_template("Show.html")

@app.route("/users/show/<int:id>")
def user_show_id(id):
   data = {
      'id': id
   }
   one_user= User.get_one(data)
   print(one_user)
   return render_template("Show.html", one_user=one_user)

# Delete User
@app.route("/users/delete/<int:user_id>")
def delete_user(user_id):
   User.delete(user_id)
   return redirect("/users")

# Edit User
@app.route("/users/edit/<int:id>")
def edit_user(id):
   data = {
      'id': id
   }
   one_user = User.get_one(data)
   return render_template("Edit.html", one_user=one_user)


# Update User

@app.route("/users/update/<int:id>", methods=['POST'])
def update_user(id):
   data = {
      'id': id,
      **request.form
   }
   User.update(data)
   return redirect("/users")