from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import API.quote as quote
import API.user as user

app = Flask(__name__)
api = Api(app)

#Регистрация API для цитат
api.add_resource(quote.Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

#Регистрация API для пользователей
api.add_resource(user.User, "/ai-users", "/ai-users/", "/ai-users/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)