#!/usr/bin/env python
# coding=utf-8

import os


def read(file_path):
    dollar_list = []

    with open(file_path) as f:
        dollar_list = [i.strip() for i in f.readlines()]

    return dollar_list


def write(file_path):
    with open(file_path, 'w') as f:
        f.write(os.linesep.join([str(i) for i in range(10)]))
