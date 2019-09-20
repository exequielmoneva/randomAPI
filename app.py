from flask import Flask
from flask_restful import reqparse
import requests

app = Flask(__name__)


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


def email(d):  # EXTRACT THE E-MAIL INFORMATION
    mail = str(d["email"])
    return mail


@app.route('/')
def local():
    return "System is up"


@app.route('/users', methods=['POST'])
def main():
    parser = reqparse.RequestParser()
    parser.add_argument("user_id")  # TAKE THE ID FROM THE BODY OF THE POST
    args = parser.parse_args()  # SAVE THE ARGUMENTS IN ORDER TO USE THEM LATER
    if args["user_id"] is None or args["user_id"].strip() == "":  # HAS A VALUE
        return "user_id is mandatory", 400
    if not args["user_id"].strip().isdigit():  # USER_ID IS WHOLE NUMBER
        return "user_id must be a whole number", 400
    r = requests.get('https://randomuser.me/api/?ud=', params=args["user_id"])  # GET INFO FROM THE PAGE
    data = r.json()  # JSON FORMATTING
    d = list(data['results'])  # GET THE DATA FROM 'results'
    direccion = direc(dict(d[0]))  # GET THE DIRECTION
    nombre = name(dict(d[0]))  # GET THE FULL NAME
    imagen = img(dict(d[0]))  # GET THE IMAGE
    correo = email(dict(d[0]))  # GET THE E-MAIL
    user = {"user": {
        "Lastname": nombre[0],
        "Firstname": nombre[1],
        "E-Mail": correo,
        "Picture": imagen,
        'Address': {
            "Street": direccion[0],
            "City": direccion[1]}
    }
    }

    return user, 200


if __name__ == '__main__':
    app.run()
