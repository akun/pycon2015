#!/usr/bin/env python
# coding=utf-8

import os
import unittest

from pycon2015.file_rw import read, write


class FileTestCase(unittest.TestCase):

    test_dir = os.path.dirname(os.path.abspath(__file__))


class FileReadTestCase(FileTestCase):

    def test_read(self):
        file_path = os.path.join(self.test_dir, 'money.txt')
        money_list = read(file_path)

        self.assertEqual(money_list, ['1', '2', '3', '4'])
        self.assertItemsEqual(money_list, ['4', '1', '2', '3'])


class FileWriteTestCase(FileTestCase):

    def setUp(self):
        self.file_path = os.path.join(self.test_dir, 'money_w.txt')

    def tearDown(self):
        if os.path.isfile(self.file_path):
            os.unlink(self.file_path)

    def test_write(self):
        write(self.file_path)

        money_list = []
        with open(self.file_path) as f:
            money_list = [i.strip() for i in f.readlines()]

        self.assertEqual(money_list, [str(i) for i in range(10)])
