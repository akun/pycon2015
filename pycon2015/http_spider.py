#!/usr/bin/env python
# coding=utf-8

import requests


def get_url_data(url):
    response = requests.get(url)

    return {i: getattr(response, i) for i in (
        'status_code',
        'headers',
        'encoding',
        'text',
    )}
