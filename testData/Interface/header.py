# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/26 17:25
# @Author  : wangqunsong
# @Email   : wangqunsong@hotmail.com
# @File    : header.py
# @Software: PyCharm
"""

from utils.base.generator import *


class Header(object):
    '''
    请求报文头类
    '''
    headers = {
        "accept-encoding": "gzip, deflate",
        "connection": "Keep-Alive",
        "content-type": "application/json",
        "host": "10.10.10.185:10003"
    }


if __name__ == '__main__':
    h = Header().headers
    print(h)