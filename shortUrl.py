#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def dwz(targetUrl):
    r = requests.get('http://985.so/api.php?url=%s' % targetUrl)
    r.encoding = 'utf-8'
    return r.text

if __name__ == '__main__':
    # print(generate('http://baidu.com'))
    print(dwz('http://baidu.com'))