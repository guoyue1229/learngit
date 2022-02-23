# coding:utf-8

import  unittest

from test_unnitests import Test

import HTML_function

def Case_Run():
    suite = unittest.TestSuite()
    suite.addTest(Test('test_V2_GetVersionV2'))

if __name__ == '__main__':
    Case_Run()