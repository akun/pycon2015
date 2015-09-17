#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient


class Book(object):

    def __init__(self, db='pycon2015'):
        self.collection = MongoClient()[db].book

    def create(self, book):
        self.collection.insert_one(book)

    def read(self, name):
        return self.collection.find_one({'name': name})

    def update(self, name, new_name):
        self.collection.update_one(
            {'name': name}, {'$set': {'name': new_name}}
        )

    def delete(self, name):
        self.collection.delete_one({'name': name})
