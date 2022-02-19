from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def home():
    users = User.get_all()
    for user in users:
        print(user)
    return render_template('read.html', all_users=users)


@app.route('/create')
def create():
    return render_template('/create.html')


@app.route('/user/<int:id>')
def show_record(id):
    data = {
        'id': id
    }
    return render_template("read_one.html", user=User.show(data))


# action route
@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "eml" : request.form["eml"],
    }
    id=User.save(data)
    return redirect('/user/'+str(id))


@app.route('/user/<int:id>/edit') 
def edit(id):
    data = {
        'id': id,
    }
    return render_template("edit.html", user=User.show(data))


@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    data = {
        'id' : id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "eml" : request.form["eml"],
    }
    User.update(data)
    return redirect('/user/'+str(id))
# +str(id) this is a python native method, that changes the type into a string. Int into a Str

@app.route('/delete/<int:id>') 
def delete(id):
    data = {
        'id': id,
    }
    User.delete(data)
    return redirect('/')
