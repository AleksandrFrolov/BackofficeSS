import logging
from flask import request
import requests

from app.handlers import BaseHandler
import app.models.translation_queries as tq


class TranslationHandler(BaseHandler):

    def post(self):
        """
        {
            'text': str,
            'from': str,
            'to': str,
            'provider': str
        }
        """
        data = request.get_json()

        try:
            query_text = data['text']
            query_language = data['from']
            translated_language = data['to']
            provider = data['provider']
        except KeyError:
            logging.debug('Bad request: %s' % data)
            return self.bad_response('Bad request')

        # TODO: add list of translated words.
        translations = self._get_translate(query_language + '-' + translated_language, query_text, provider)
        for translated_text in translations:
            new_translation = tq.add_translation(query_text, query_language, translated_text, translated_language, provider)
            if new_translation is None:
                logging.debug('Db save error')
                return self.bad_response('Internal error')

    def _get_translate(self, lang_direct, text, url):
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        data = {
            'key': '',
            'text': text,
            'lang': lang_direct
        }
        req = requests.post(url, data=data, headers=headers)
        res = req.json()
        if res.code == 200:
            return res['text']
        else:
            logging.debug('Translate error: %s' % res.code)
            return None


