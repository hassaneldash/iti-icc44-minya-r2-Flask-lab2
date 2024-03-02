from bson import ObjectId
from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__,template_folder = 'templates')
app.config["MONGO_URI"]="mongodb://127.0.0.1:27017/flask"
mongo=PyMongo(app)

@app.route('/')
def user_list():
    data = list(mongo.db.Users.find({}))
    return render_template('users.html', users=data)

@app.route('/createuser')
def createuser():
    return render_template('create_user.html')

@app.route('/users', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        location = request.form.get('location')
        if name and age and location: 
            mongo.db.Users.insert_one({'name': name, 'age': age, 'location': location})
    data = list(mongo.db.Users.find({}))  
    return render_template('users.html', users=data) 

@app.route('/edit_user/<string:_id>', methods=['GET', 'POST'])
def edit_user(_id):
    user = mongo.db.Users.find_one({'_id':ObjectId(_id) })
    if request.method == 'POST':
        user['name'] = request.form.get('name')
        user['location'] = request.form.get('location')
        user['age'] = request.form.get('age')
        mongo.db.Users.update_one({'_id': ObjectId(_id)}, {'$set': user})
        return redirect('/users')
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<string:_id>')
def delete_user(_id):
    mongo.db.Users.delete_one({'_id': ObjectId(_id)})
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)

