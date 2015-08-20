#!/usr/bin/env python
# coding=utf-8

import unittest

from pycon2015.hello_world import add


class HelloWorldTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, add(1, 1))
        self.assertNotEqual(2, add(-1, -1))
