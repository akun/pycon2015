#!/usr/bin/env python
# coding=utf-8

import os


def read_dollar(file_path):
    dollar_list = []

    with open(file_path) as f:
        dollar_list = [i.strip() for i in f.readlines()]

    return dollar_list


def write_rmb(file_path, rmb_list=None):
    if rmb_list is None:
        rmb_list = []

    with open(file_path, 'w') as f:
        f.write(os.linesep.join([str(i) for i in rmb_list]))
