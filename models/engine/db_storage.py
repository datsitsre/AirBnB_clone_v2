#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base

from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pword = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pword, host, db_name
        )
        self.__engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True
        )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def close(self):
        """ calls remove()
        """
        self.__session.close()
