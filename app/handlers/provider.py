import logging
from flask import request

from app.handlers import BaseHandler
import app.models.provider_queries as pq


class ProviderHandler(BaseHandler):

    def get(self):
        """
        Get providers list.
        """
        providers = pq.get_providers()
        if not providers:
            return self.bad_response('Internal error')
        res = [{'id': p.id, 'title': p.title, 'link': p.link} for p in providers]
        return self.success_response({'providers': res})

    def post(self):
        """
        {
            'title': str,
            'link': str
        }
        """
        data = request.get_json()

        title = data.get('title')
        link = data.get('link')
        if not title or not link:
            logging.debug('Bad request: %s' % data)
            return self.bad_response('Bad request')

        new_provider = pq.add_provider(title, link)
        if new_provider is None:
            return self.bad_response('Internal error')

        return self.success_response(data)
