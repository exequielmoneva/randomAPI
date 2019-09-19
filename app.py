import collections
from flask import Flask, jsonify
from flask_restful import reqparse
import requests
from collections import OrderedDict
import json

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def main():
    parser = reqparse.RequestParser()
    parser.add_argument("user_id")  # TAKE THE ID FROM THE BODY OF THE POST
    args = parser.parse_args()  # SAVE THE ARGUMENTS IN ORDER TO USE THEM LATER
    r = requests.get('https://randomuser.me/api/?ud=', params=args["user_id"])  # GET INFO FROM THE PAGE
    data = r.json()  # JSON FORMATTING
    #response = requests.put('https://randomuser.me/api/?ud=', params=args["user_id"])
    d = list(data['results'])  # GET THE DATA FROM 'results'
    direccion = direc(dict(d[0]))  # GET THE DIRECTION
    nombre = name(dict(d[0]))  # GET THE FULL NAME
    imagen = img(dict(d[0]))  # GET THE IMAGE
    user = {"user": {
        "lastname": nombre[0],
        "firstname": nombre[1],
        "image": imagen,
        'address': {
            "street": direccion[0],
            "city": direccion[1]}
    }
    }

    return user, 200


def direc(d):  # EXTRACT THE ADDRESS INFORMATION
    ret = []
    street = str(d['location']['street'])
    ret.append(street)
    city = str(d['location']['city'])
    city += " - {}".format(str(d['location']['state']))
    ret.append(city)
    return ret


def name(d):  # EXTRACT NAME INFORMATION
    ret = []
    lastname = str(d['name']['last'])
    ret.append(lastname)
    firstname = str(d['name']['first'])
    ret.append(firstname)
    return ret


def img(d):  # EXTRACT THE IMAGE INFORMATION
    image = str(d['picture']['large'])
    return image


if __name__ == '__main__':
    app.run()
