import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app import app

db = SQLAlchemy(app)


class Providers(db.Model):
    __tablename__ = 'providers'

    id = Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    title = Column(String(length=50), nullable=False, index=True)
    link = Column(String(length=100), nullable=False)
    date_created = Column(DateTime)
    active = Column(Boolean, default=True)

    translations = db.relationship('Translations', backref='provider')

    def __init__(self, title, link, date_created, active):
        self.title = title
        self.link = link
        self.date_created = date_created
        self.active = active

    def __repr__(self):
        return self.title


class Languages(db.Model):
    __tablename__ = 'languages'

    id = Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    name = Column(String(length=100), nullable=False, index=True)
    date_created = Column(DateTime)
    active = Column(Boolean, default=True)

    def __init__(self, name, date_created, active):
        self.name = name
        self.date_created = date_created
        self.active = active

    def __repr__(self):
        return self.name


class Translations(db.Model):
    __tablename__ = 'translations'

    id = Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    query_text = Column(Text, nullable=False)
    query_language_id = Column(UUID, ForeignKey('languages.id'), nullable=False)
    translated_text = Column(Text, nullable=False)
    translated_language_id = Column(UUID, ForeignKey('languages.id'), nullable=False)
    provider_id = Column(UUID, ForeignKey('providers.id'), nullable=False)
    date_created = Column(DateTime)

    def __init__(self, query_text, query_language, translated_text, translated_language, provider, date_created):
        self.query_text = query_text
        self.query_language = query_language
        self.translated_text = translated_text
        self.translated_language = translated_language
        self.provider = provider
        self.date_created = date_created

    def __repr__(self):
        return self.id
