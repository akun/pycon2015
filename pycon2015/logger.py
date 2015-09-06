#!/usr/bin/env python
# coding=utf-8

import logging


def show_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    logger.debug('I am DEBUG')
    logger.info('I am INFO')
    logger.warning('I am WARNING')
    logger.error('I am ERROR')
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception('I am EXCEPTION')
    logger.critical('I am CRITICAL')
