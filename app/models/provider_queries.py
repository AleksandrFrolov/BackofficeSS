import logging
import datetime as dt

from app.models import db, Providers


def get_providers():
    try:
        providers = Providers.query.filter(
            Providers.active == True
        ).order_by(Providers.title).all()
        return providers
    except Exception as e:
        logging.error(e)
        return None


def add_provider(title, link):
    try:
        provider = Providers(title=title, link=link, date_created=dt.datetime.now(), active=True)
        db.session.add(provider)
        db.session.commit()
        return provider
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        return None
