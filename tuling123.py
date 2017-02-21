#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib.parse
import urllib.request
import json

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def ask(question):
    key = 'fc6acc04096a4a9f81cb0c447f54009a'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    request = api + urllib.parse.quote(question)
    response = getHtml(request)
    dic_json = json.loads(response.decode())
    return dic_json['text']

if __name__ == '__main__':

    # key = 'fc6acc04096a4a9f81cb0c447f54009a'
    # api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        info = input('我: ')
        # request = api + urllib.parse.quote(info)
        # response = getHtml(request)
        # dic_json = json.loads(response.decode())
        # print('贾维斯：' + dic_json['text'])
        print('贾维斯：' + ask(info))