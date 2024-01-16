#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of City instances"""
            from models import storage
            list_of_cities = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    list_of_cities.append(value)
            return list_of_cities
