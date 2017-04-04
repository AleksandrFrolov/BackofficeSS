from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.CONFIG')

api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


def add_api(handler, url):
    api.add_resource(handler, '/' + url)


"""
POST /translation
GET /languages
GET /providers
GET /statistics
"""

from app.handlers.translation import TranslationHandler
add_api(TranslationHandler, 'translation')

from app.handlers.language import LanguageHandler
add_api(LanguageHandler, 'languages')

from app.handlers.provider import ProviderHandler
add_api(ProviderHandler, 'providers')
