from flask import request
from flask_restx import Resource, Namespace
from server.session import read, write
import json

from .auth import uniq_strings


api = Namespace("rename")


@api.route("/user/<name>")
class Auth(Resource):
    def post(self, name):
        uniq = request.json["auth"]
        new_name = request.json["name"]
        data = read()
        if uniq in uniq_strings:
            if name in data["name"]:
                f = open("users.json", "w", encoding="UTF-8")
                i = data["name"].index(name)
                data["name"][i] = new_name
                write(data)
                return str(data["name"][i])
            else:
                return "Error: wrong name"
        else:
            return "Error: not authorized"
