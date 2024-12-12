import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False) 
    created_at = Column(DateTime, nullable=False)
    favorites = relationship("Favorite", back_populates="user")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    gender = Column(String(50))
    birth_year = Column(String(20))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship("Planet", back_populates="residents")
    description = Column(String(500))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    climate = Column(String(100))
    population = Column(String(50))
    residents = relationship("Character", back_populates="homeworld")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    created_at = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
