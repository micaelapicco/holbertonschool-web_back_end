#!/usr/bin/env python3
"""
Task 8:
lists all documents in a collection
"""


def list_all(mongo_collection):
    """list all documents in a collection"""
    return mongo_collection.find()
