from flask import Flask
from flask_restful import Api
import API.endpoints as endpoints
import API.config as cfg

app = Flask(__name__)
api = Api(app)

endpoints.addEndPoints(api)

if __name__ == '__main__':
    app.run(
        host = cfg.SERVER_HOST, 
        port = cfg.SERVER_PORT, 
        debug = True
    )