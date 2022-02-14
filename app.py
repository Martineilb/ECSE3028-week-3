from flask import Flask
from flask_pymongo import PyMongo
from marshmallow import Schema, fields
from bson.json_util import dumps
from json import loads 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://week3:<password>@cluster0.rzize.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

class FruitSchema(Schema):
    name = fields.String(required=True)
    sugar_content = fields.Integer()
    colour = fields.color(required=True)
    country = fields.String(required=True)


@app.route("/fruit", methods=["POST"])
def add_new_fruit():
    request_dict = request.json
    new_fruit = FruitSchema.load(request_dict)


    fruit_document = mongo.db.fruits.insert_one(new_fruit) 
    fruit_id = fruit_document.inserted_id

    fruit = mongo.db.fruits.find_one({"_id": fruit_id})

    fruit_json = loads(dumps(fruit))

    return jsonify(fruit_json)