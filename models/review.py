#!/usr/bin/python3
"""the review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the review class"""

    place_id = ""
    user_id = ""
    text = ""
