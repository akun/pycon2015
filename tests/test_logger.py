#!/usr/bin/env python
# coding=utf-8

import unittest

from testfixtures import log_capture

from pycon2015.logger import show_logger


class LoggerTestCase(unittest.TestCase):

    @log_capture()
    def test_show_logger(self, log_capture):
        show_logger()

        log_capture.check(
            # ('pycon2015.logger', 'DEBUG', 'I am DEBUG'),
            # ('pycon2015.logger', 'INFO', 'I am INFO'),
            ('pycon2015.logger', 'WARNING', 'I am WARNING'),
            ('pycon2015.logger', 'ERROR', 'I am ERROR'),
            ('pycon2015.logger', 'ERROR', 'I am EXCEPTION'),
            ('pycon2015.logger', 'CRITICAL', 'I am CRITICAL'),
        )
