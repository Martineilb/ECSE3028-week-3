from flask import flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://week3:<password>@cluster0.rzize.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)