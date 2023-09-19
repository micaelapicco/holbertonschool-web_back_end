#!/usr/bin/env python3
"""
Task 9:
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    output = mongo_collection.insert_one(kwargs)
    return output.inserted_id
