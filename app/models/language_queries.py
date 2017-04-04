import logging
import datetime as dt
from app.models import db, Languages


def get_languages():
    try:
        languages = Languages.query.filter(
            Languages.active == True
        ).order_by(Languages.name).all()
        return languages
    except Exception as e:
        logging.error(e)
        return None


def add_language(name):
    try:
        language = Languages(name=name, date_created=dt.datetime.now(), active=True)
        db.session.add(language)
        db.session.commit()
        return language
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        return None
