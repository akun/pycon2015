#!/usr/bin/env python
# coding=utf-8

import unittest

import httpretty

from pycon2015.http_spider import get_url_data


class HttpSpiderTestCase(unittest.TestCase):

    @unittest.skip('Fuck GFW')
    def test_get_url_data_impossible_in_china(self):
        url_data = get_url_data('http://www.google.com/')

        self.assertEqual(url_data['status_code'], 200)
        self.assertEqual(url_data['encoding'], 'utf-8')

    @httpretty.activate
    def test_get_url_data(self):
        url = 'http://www.google.com/'
        httpretty.register_uri(
            httpretty.GET, url, body='Fake Google', status=200
        )
        url_data = get_url_data(url)

        self.assertEqual(url_data['status_code'], 200)
        self.assertEqual(url_data['encoding'], 'utf-8')
