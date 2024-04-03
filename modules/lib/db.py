from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL = config('DB_URL', default="sqlite:///db/data.db")

echo = config('DEBUG', default=False, cast=bool)
engine = create_engine(DB_URL, echo=echo)


Session = scoped_session(sessionmaker(bind=engine))