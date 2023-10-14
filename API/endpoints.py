'''Модуль регистрации конечных точек API сервиса'''
import API.quote as quote
import API.user as user
import dba.exception as ex

def addEndPoints(api):
    '''Регистрация конечных точек API сервиса'''
    #Регистрация API для цитат
    api.add_resource(quote.Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

    #Регистрация API для пользователей
    api.add_resource(user.User, "/ai-users", "/ai-users/", "/ai-users/<int:id>")

    if not api:
        raise ex.UserNotFoundException('error')