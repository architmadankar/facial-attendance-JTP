from typing import List
from datetime import date as dt, datetime as dtime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from modules.db import Session

DBase = declarative_base()

class AdminModel(DBase):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    @classmethod
    def find_by_username(cls, username: str) -> "AdminModel":
        return Session.query(cls).filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "AdminModel":
        return Session.query(cls).filter_by(id=_id).first()

    def create(self) -> None:
        Session.add(self)
        Session.commit()

    def delete(self) -> None:
        Session.delete(self)
        Session.commit()

class UserModel(DBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    attendances = relationship(
        "AttendanceModel",
        backref=backref("user")
    )

    @classmethod
    def find_by_name(cls, name: str) -> "UserModel":
        return Session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return Session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return Session.query(cls).all()

    def create(self) -> None:
        Session.add(self)
        Session.commit()

    def delete(self) -> None:
        Session.delete(self)
        Session.commit()

class AttendanceModel(DBase):
    __tablename__ = "attendances"

    date = Column(DateTime(timezone=True), default=dtime.now, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    @classmethod
    def find_by_date(cls, date: dt, user: UserModel) -> "AttendanceModel":
        return Session.query(cls).filter_by(date=date, user=user).first()

    @classmethod
    def find_by_user(cls, user: UserModel) -> "AttendanceModel":
        return Session.query(cls).filter_by(user=user).first()

    @classmethod
    def find_by_time(cls, time: dtime) -> "AttendanceModel":
        return Session.query(cls).filter_by(time=time).first()

    @classmethod
    def find_all(cls) -> List["AttendanceModel"]:
        return Session.query(cls).all()

    @classmethod
    def is_marked(cls, date: dt, user: UserModel) -> bool:
        marked = AttendanceModel.find_by_date(date, user)
        if marked is None:
            marked = False
        else:
            marked = True
        return marked

    def create(self) -> None:
        Session.add(self)
        Session.commit()

    def delete(self) -> None:
        Session.delete(self)
        Session.commit()

class VideoModel(DBase):
    __tablename__ = "video_feeds"

    id = Column(String(30), nullable=False, primary_key=True)
    is_active = Column(Boolean, default=False)
    url = Column(String, nullable=False)

    @classmethod
    def find_by_id(cls, _id: str) -> "VideoModel":
        return Session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_url(cls, url: str) -> "VideoModel":
        return Session.query(cls).filter_by(url=url).first()

    @classmethod
    def find_all(cls) -> List["VideoModel"]:
        return Session.query(cls).all()

    def create(self) -> None:
        Session.add(self)
        Session.commit()

    def delete(self) -> None:
        Session.delete(self)
        Session.commit()