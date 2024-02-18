#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """State class / table model"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def cities(self):
            """The cities property"""
            all_storage = models.storage.all(models.City)
            return [city for city in all_storage.values() if city.state_id == self.id]
    else:
        cities = relationship("City", cascade="all, delete", backref="state")
