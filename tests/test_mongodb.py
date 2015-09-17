#!/usr/bin/env python
# coding=utf-8

import os
import subprocess
import unittest

from pymongo import MongoClient

from pycon2015.mongodb import Book


class BookTestCase(unittest.TestCase):

    def setUp(self):
        # mongoexport -d pycon2015 -c book > tests/book.json
        # mongoimport -d test_pycon2015 -c book < tests/book.json

        self.test_db = 'test_pycon2015'
        self.client = MongoClient()
        self.collection = self.client[self.test_db].book

        test_dir = os.path.dirname(os.path.abspath(__file__))
        test_data_path = os.path.join(test_dir, 'book.json')

        p = subprocess.Popen(
            'mongoimport -d %(test_db)s -c book < %(test_data_path)s' % {
                'test_db': self.test_db,
                'test_data_path': test_data_path,
            },
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        p.communicate()

        self.book = Book(self.test_db)

    def tearDown(self):
        self.client.drop_database(self.test_db)

    def test_create(self):
        before_count = self.collection.count()
        self.book.create({'name': 'Dive Into Python 3'})
        after_count = self.collection.count()

        self.assertEqual(before_count + 1, after_count)

    def test_read(self):
        book_name = 'Python Cookbook'
        book = self.book.read(name=book_name)

        self.assertEqual(book['name'], book_name)

    def test_update(self):
        old_book_name = 'Dive Into Python'
        new_book_name = 'Dive Into Python 3'

        before_count = self.collection.find({'name': old_book_name}).count()
        self.book.update(name=old_book_name, new_name=new_book_name)
        after_count = self.collection.find({'name': old_book_name}).count()
        new_book = self.collection.find_one({'name': new_book_name})

        self.assertEqual(before_count, 1)
        self.assertEqual(after_count, 0)
        self.assertEqual(new_book['name'], new_book_name)

    def test_delete(self):
        before_count = self.collection.count()
        self.book.delete(name='Learn Python The Hard Way')
        after_count = self.collection.count()

        self.assertEqual(before_count - 1, after_count)
