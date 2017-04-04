import logging
import datetime as dt

from app.models import db, Translations


def add_translation(query_text, query_language, translated_text, translated_language, provider):
    try:
        translation = Translations(
            query_text=query_text, query_language=query_language,
            translated_text=translated_text, translated_language=translated_language,
            provider=provider, date_created=dt.datetime.now()
        )
        db.session.add(translation)
        db.session.commit()
    except Exception as e:
        logging.error(e)
        db.session.rollback()
        return None
