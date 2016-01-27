#!/usr/bin/env python
#coding:utf-8
import sys
import tornado.web

reload(sys)
sys.setdefaultencoding('utf-8')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello world')

