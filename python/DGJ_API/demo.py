# coding:utf-8
import json

import requests
import unittest

Token = None  # 全局授权


class Case(unittest.TestCase):

    def test_VerificationAvailable(self):
        data = {
            "ReqTime": "1606722821891",
            "BelongCompanyId": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": "t812btdrct7f1y0ob7wj",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Signature": "C98716A205795A2097992B06B58BB103",
            "AccountType": "20",
            "AppID": "0",
            "TerminalType": "Android"
        }
        header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json', 'accept': 'application/json',
                  'authorization': 'Bearer ' + str(Token)}
        response = requests.post('https://butlerapp.diyibox.com/User/VerificationAvailable', data=json.dumps(data),
                                 headers=header)
        self.assertEqual(response.status_code, 200, '返回状态错误，不为200')
        print(response.text)
