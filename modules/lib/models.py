from datetime import date as d, datetime as dt
from typing import List

from modules.db import Session

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Boolean, DateTime, ForeignKey

DBase=declarative_base()


class VideoModel(DBase):
    __tablename__ = "video"
    id = Column(String(30), nullable=False, primary_key=True)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    @classmethod
    def get_by_id(cls, _id: int) -> "VideoModel":
        return Session.query(cls). filter_by(id=id).first()
    
    @classmethod
    def get_by_url(cls, url: str) -> "VideoModel":
        return Session.query(cls). filter_by(url=url).first()
    
    @classmethod
    def findall(cls) -> List["VideoModel"]:
        return Session.query(cls).all() 
    
    def create(self) -> None:
        Session.add(self)
        Session.commit()
    
    def remove(self) -> None:
        Session.delete(self)
        Session.commit()
        
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

class MarkAttendance(DBase):
    __tablename__ = "marked"
    date = Column(DateTime(timezone=True), default=dt.now, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    @classmethod
    def getall(cls) -> List["MarkAttendance"]:
        return Session.query(cls).all()
    
    def create(self) -> None:
        Session.add(self)
        Session.commit()
    
    def remove(self) -> None:
        Session.delete(self)
        Session.commit()
        
    @classmethod
    def find_by_date(cls, date: d, user: User) -> "MarkAttendance":
        return Session.query(cls).filter_by(date=date, user=user).first()
    
    @classmethod
    def get_by_time(cls, time:dt) -> "MarkAttendance":
        return Session.query(cls).filter_by(time=time).first()
    
    @classmethod
    def get_by_user(cls, user: User) -> "MarkAttendance":
        return Session.query(cls).filter_by(user=user).first()
    
    @classmethod
    def is_marked(cls, date: d, user: User) -> bool:
        marked = MarkAttendance.find_by_date(date, user)
        if marked is None:
            marked = False
        else:
            marked= True
            return marked
        