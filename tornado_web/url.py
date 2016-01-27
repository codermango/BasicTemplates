#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.main import MainHandler


url = [
    (r'/', MainHandler)
]