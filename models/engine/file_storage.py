#!/usr/bin/python3
""" Flask storage file """
import os
import json
from importlib import import_module


class FileStorage:
    """ Class Instance storage """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ Instance the class """
        self.model_classes = { 
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }
        
        def close(self):
            """ Close the storage """
            self.reload()
