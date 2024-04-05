from datetime import date as d, datetime as dt
from typing import List

from modules.db import Session

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref


DBase=declarative_base()

class AdminModel(DBase):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

    @classmethod
    def get_username(cls, username: str) -> "AdminModel":
        return Session.query(cls).filter_by(username=username).first()

    @classmethod
    def get_id(cls, _id: int) -> "AdminModel":
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
    records = relationship(
        "MarkAttendanceModel",
        backref=backref("user")
    )

    @classmethod
    def get_name(cls, name: str) -> "UserModel":
        return Session.query(cls).filter_by(name=name).first()

    @classmethod
    def get_id(cls, _id: int) -> "UserModel":
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

class MarkAttendanceModel(DBase):
    __tablename__ = "records"

    date = Column(DateTime(timezone=True), default=dt.now, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"))

    @classmethod
    def get_date(cls, date: d, user: UserModel) -> "MarkAttendanceModel":
        return Session.query(cls).filter_by(date=date, user=user).first()

    @classmethod
    def get_student(cls, user: UserModel) -> "MarkAttendanceModel":
        return Session.query(cls).filter_by(user=user).first()

    @classmethod
    def get_time(cls, time: dt) -> "MarkAttendanceModel":
        return Session.query(cls).filter_by(time=time).first()

    @classmethod
    def find_all(cls) -> List["MarkAttendanceModel"]:
        return Session.query(cls).all()

    @classmethod
    def is_marked(cls, date: d, user: UserModel) -> bool:
        marked = MarkAttendanceModel.get_date(date, user)
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
    __tablename__ = "video_dat"

    id = Column(String(30), nullable=False, primary_key=True)
    is_active = Column(Boolean, default=False)
    url = Column(String, nullable=False)

    @classmethod
    def get_id(cls, _id: str) -> "VideoModel":
        return Session.query(cls).filter_by(id=_id).first()

    @classmethod
    def get_url(cls, url: str) -> "VideoModel":
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