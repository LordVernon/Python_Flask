from flask_restx import Resource, Namespace
from server.session import read


api = Namespace("users")


@api.route("/users")
class Users(Resource):
    def get(self):
        data = read()
        return data["name"]
