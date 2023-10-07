from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

ai_users = [
    {
        "id": 1,
        "name": "Anton",
        "role": "Administrator"
    },
    {
        "id": 2,
        "name": "Andrew",
        "role": "System administrator"
    },
    {
        "id": 3,
        "name": "Max",
        "role": "Gamer"
    },
    {
        "id": 4,
        "name": "Nataly",
        "role": "Manager"
    }
]


class User(Resource):
    def get(self, id=0):       
        if id == 0:
            return random.choice(ai_users), 200
        for user in ai_users:
            if(user["id"] == id):
                return user, 200
        return "User not found", 404       
    
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("role")
        params = parser.parse_args()
        for user in ai_users:
            if(id == user["id"]):
                return f"User with id {id} already exists", 400
        user = {
            "id": int(id),
            "name": params["name"],
            "role": params["role"]
        }
        ai_users.append(user)
        return user, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("role")
        params = parser.parse_args()
        for user in ai_users:
            if(id == user["id"]):
                user["name"] = params["name"]
                user["role"] = params["role"]
                return user, 200
        
        user = {
            "id": id,
            "name": params["name"],
            "role": params["role"]
        }
        
        ai_users.append(user)
        return user, 201


    def delete(self, id):
        global ai_users
        ai_users = [user for user in ai_users if user["id"] != id]
        return f"User with id {id} is deleted.", 200