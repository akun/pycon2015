#!/usr/bin/env python
# coding=utf-8

class GenderException(Exception):
    pass

def go_to_toilet(gender):
    gender = gender.lower()
    show_msg = None

    if gender in ('man', 'boy'):
        show_msg = 'Man Toilet'
    elif gender in ('woman', 'girl'):
        show_msg = 'Woman Toilet'
    else:
        raise GenderException

    return show_msg
