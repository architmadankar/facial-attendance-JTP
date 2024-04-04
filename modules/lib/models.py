from datetime import date as d, datetime as dt
from modules.db import Session

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
DBase=declarative_base()


class Admin(DBase):
    __tablename__ = "admins"
    