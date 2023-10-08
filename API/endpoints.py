'''Модуль регистрации конечных точек API сервиса'''
import API.quote as quote
import API.user as user

def addEndPoints(api):
    '''Регистрация конечных точек API сервиса'''
    #Регистрация API для цитат
    api.add_resource(quote.Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

    #Регистрация API для пользователей
    api.add_resource(user.User, "/ai-users", "/ai-users/", "/ai-users/<int:id>")