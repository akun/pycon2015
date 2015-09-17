#!/usr/bin/env python
# coding=utf-8

import unittest

from sqlalchemy.ext.declarative import declarative_base

from pycon2015.sql import DatabaseProduct, Product


class DatabaseProductTestCase(unittest.TestCase):

    product_list = [
        'Cassandra', 'CouchDB', 'MariaDB', 'MongoDB', 'MySQL',
        'PostgreSQL', 'Redis',
    ]

    def setUp(self):
        self.dbp = DatabaseProduct()

        for name in self.product_list:
            product = Product(name=name)
            self.dbp.session.add(product)

        self.dbp.session.commit()

    def tearDown(self):
        Base = declarative_base()
        Base.metadata.drop_all(self.dbp.engine)

    def test_vote(self):
        redis = self.dbp.session.query(Product).filter_by(name='Redis').first()
        before_vote = redis.vote
        self.dbp.vote('Redis')
        after_vote = redis.vote

        self.assertEqual(before_vote, 0)
        self.assertEqual(after_vote, 1)
