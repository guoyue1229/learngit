# coding:utf-8
import unittest

import requests

import json


# from HTML_function import *

class Test(unittest.TestCase):
    Token = None
    header = None
    host = "http://butlerapp-test.diyibox.com"
    express = "JT2021090720001"

    # 测试开始
    @classmethod
    def setUpCalss(cls):
        # 登陆获取Token
        url = cls.host + '/User/Login'
        header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json', 'accept': 'application/json',
                  'authorization': 'Bearer '}
        data = {
            "Nonce": "nt3qko2nxlchdn37kfwb",
            "ReqTime": "1631003203381",
            "TerminalType": "Android",
            "AppID": "10100",
            "Phone": "18838202844",
            "Signature": "92D9BC032721E58DAFB6EEE6ECA58884",
            "TerminalVersion": "1.6.9t4",
            "Password": "Lq5GTgx6DfQ="
        }
        # data['Signature'] = Getsgin(data)
        response = requests.post(url, data=json.dumps(data), headers=header)
        if response.ok is True:
            cls.Token = response.json()['Data']['Token']  # 设置Token
            cls.header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json;charset=utf-8',
                          'accept': 'application/json',
                          'authorization': 'Bearer ' + str(cls.Token)}
        else:
            print("登陆失败")
            # 准备发送邮箱
            return

    def test_V2_GetVersionV2(self):
        url = self.host + '/V2/APP/GetVersionV2'
        header =
        data = {
            "Nonce": "etxafxsg0m7zzdnoc0g3",
            "ReqTime": "1631005756855",
            "TerminalType": "Android",
            "AppID": "10100",
            "Signature": "FA703F379B4EA2F8A554ACD2217D521E",
            "SystemType": "1",
            "StationId": "88689960",
            "TerminalVersion": "1.6.9t4"
        }
        response = requests.post(url, headers=self.header, data=json.dumps(data))
        print(json.dumps(data))
        print(response.text)
        print(self.header)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')
