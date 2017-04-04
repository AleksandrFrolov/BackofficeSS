from flask_restful import Resource
from flask_responses import json_response


class BaseHandler(Resource):
    def __init__(self):
        self._partner = None

    def success_response(self, data):
        return json_response(data, status_code=200)

    def bad_response(self, message):
        return json_response({"message": message}, status_code=400)
