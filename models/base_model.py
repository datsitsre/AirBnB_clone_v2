#!/usr/bin/python3
"""
Class BaseModel
Definitions
"""

import os
import json
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """The BaseModel class Derivitives"""
    def __init__(self, *args, **kwargs):
        if not kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                   setattr(self, key, value)
                if "id" not in kwargs:
                   self.id = str(uuid.uuid4())
                if "created_at" not in kwargs:
                   self.created_at = datetime.now()
                if "updated_at" not in kwargs:
                   self.updated_at = datetime.now()
        else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
