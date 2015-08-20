#!/usr/bin/env python
# coding=utf-8

import unittest

from pycon2015.raise_exception import GenderException, go_to_toilet


class RaiseExceptionTestCase(unittest.TestCase):

    def test_go_to_toilet(self):
        for i in ('MAN', 'BOY'):
            show_msg = go_to_toilet(i)
            self.assertEqual('Man Toilet', show_msg)

        for i in ('WOMAN', 'GIRL'):
            show_msg = go_to_toilet(i)
            self.assertEqual('Woman Toilet', show_msg)

        with self.assertRaises(GenderException):
            go_to_toilet('baby')
