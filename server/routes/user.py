from flask import request
from flask_restx import Resource, Namespace
from server.session import read, write
from datetime import datetime
import bcrypt


api = Namespace("user")


@api.route("/user")
class User(Resource):
    def post(self):
        name = request.json["name"]
        password = bytes(request.json["pass"], encoding="UTF-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
        s = hashed.decode(errors='surrogateescape')
        data = read()
        data["pass"].append(s)
        data["time"].append(str(datetime.now()))
        data["name"].append(name)
        write(data)
        return str(hashed)
