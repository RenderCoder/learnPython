#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'hello,world.'

fruits = {
    'apple': 10,
    'banana': 1,
    'pear': 2
}

print fruits['apple']

fruits['apple'] = 5
fruits['grape'] = 50
print fruits

print 'a' in fruits

print fruits.get('applex', 0)

print abs(-1000)