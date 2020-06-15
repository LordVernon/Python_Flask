from flask import request
from flask_restx import Resource, Namespace
from server.session import read
import bcrypt
import uuid

api = Namespace("auth")
uniq_strings = []


@api.route("/auth")
class Auth(Resource):
    def post(self):
        name = request.json["name"]
        password = bytes(request.json["pass"], encoding="UTF-8")
        data = read()
        if name not in data["name"]:
            return "Error: not authorized"
        i = data["name"].index(name)
        hashed = data["pass"][i].encode(errors='surrogateescape')
        if bcrypt.checkpw(password, hashed):
            uniq = str(uuid.uuid4())
            uniq_strings.append(uniq)
            return uniq
        else:
            return "Error: not authorized"
