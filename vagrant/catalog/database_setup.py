import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)



class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    last_modification = Column(DateTime, default=func.now())
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    



    


engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)