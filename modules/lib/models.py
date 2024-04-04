from datetime import date as d, datetime as dt
from typing import List

from modules.db import Session

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Boolean

DBase=declarative_base()


class Admin(DBase):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True)
    user= Column(String(30), nullable=False, unique=True)
    passwd= Column(String(30), nullable=False)
    
    @classmethod
    def get_by_id(cls, _id: int) -> "Admin":
        return Session.query(cls). filter_by(id=id).first()
    
    @classmethod
    def get_by_user(cls, user: str) -> "Admin":
        return Session.query(cls). filter_by(user=user).first()
    
    def create(self) -> None:
        Session.add(self)
        Session.commit()
    
    def remove(self) -> None:
        Session.delete(self)
        Session.commit()

class User(DBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    # todo relationships
    
    @classmethod
    def get_by_id(cls, _id: int) -> "User":
        return Session.query(cls). filter_by(id=id).first()
    
    @classmethod
    def get_by_user(cls, name: str) -> "User":
        return Session.query(cls). filter_by(name=name).first()
    
    @classmethod
    def findall(cls) -> List["User"]:
        return Session.query(cls).all()

    def create(self) -> None:
        Session.add(self)
        Session.commit()
    
    def remove(self) -> None:
        Session.delete(self)
        Session.commit()