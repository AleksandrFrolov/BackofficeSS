"""
CREATE DATABASE backoffice;

CREATE USER iqoptions WITH PASSWORD '12345';

GRANT ALL PRIVILEGES ON DATABASE backoffice TO iqoptions;

ALTER DATABASE backoffice OWNER TO iqoptions;
"""

from app.models import db

if __name__ == '__main__':
    db.create_all()
