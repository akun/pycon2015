#!/usr/bin/env python
# coding=utf-8

import os
import unittest

from mock import mock_open, patch

from pycon2015.file_rw import read_dollar, write_rmb


class FileTestCase(unittest.TestCase):

    test_dir = os.path.dirname(os.path.abspath(__file__))


class FileReadTestCase(FileTestCase):

    def test_read(self):
        file_path = os.path.join(self.test_dir, 'money.txt')
        money_list = read_dollar(file_path)

        self.assertEqual(money_list, ['1', '2', '3', '4'])
        self.assertItemsEqual(money_list, ['4', '1', '2', '3'])

    def test_read_big_file(self):
        test_list = [str(i) for i in range(12345)]
        fake_open = mock_open(read_data=os.linesep.join(test_list))
        fake_path = '/it/is/a/fake/path'

        money_list = []
        with patch('__builtin__.open', fake_open):
            money_list = read_dollar(fake_path)

        self.assertEqual(money_list, test_list)
        fake_open.assert_called_once_with(fake_path)


class FileWriteTestCase(FileTestCase):

    def setUp(self):
        self.file_path = os.path.join(self.test_dir, 'money_w.txt')

    def tearDown(self):
        if os.path.isfile(self.file_path):
            os.unlink(self.file_path)

    def test_write(self):
        write_rmb(self.file_path, range(10))

        money_list = []
        with open(self.file_path) as f:
            money_list = [i.strip() for i in f.readlines()]

        self.assertEqual(money_list, [str(i) for i in range(10)])

    def test_write_big_file(self):
        max_rmb = 12345
        fake_open = mock_open()
        fake_path = '/it/is/a/fake/path'

        with patch('__builtin__.open', fake_open):
            write_rmb(fake_path, range(max_rmb))

        fake_open.assert_called_once_with(fake_path, 'w')
        fake_open().write.assert_called_once_with(
            os.linesep.join([str(i) for i in range(max_rmb)])
        )
