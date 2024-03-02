from flask import Flask
from flask_pymongo import PyMongo
app = Flask( name )

mongo = PyMongd(app)

@app.route('/')
def index():
    data=mongo.db.Instructor.find({})
    print(data)
    return 'ok'