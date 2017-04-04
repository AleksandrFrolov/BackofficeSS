import logging
from flask import request

from app.handlers import BaseHandler
import app.models.language_queries as lq


class LanguageHandler(BaseHandler):

    def get(self):
        """
        Get language list.
        """
        language_list = lq.get_languages()
        if not language_list:
            logging.debug('Empty language list')
            return self.bad_response('Internal error')
        res = [{'id': language.id, 'language': language.name} for language in language_list]
        return self.success_response({'languages': res})

    def post(self):
        """
        {
            'name': str
        }
        """
        data = request.get_json()

        name = data.get('name')
        if not name:
            logging.debug('Bad request: %s' % data)
            return self.bad_response('Bad request')

        new_language = lq.add_language(name)
        if new_language is None:
            return self.bad_response('Internal error')

        return self.success_response(data)
