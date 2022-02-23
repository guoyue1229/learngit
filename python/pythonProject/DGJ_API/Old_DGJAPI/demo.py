# coding:utf-8
import json

import requests
import unittest

Token = None  # 全局授权


class Case(unittest.TestCase):

    def test_login(self):
        data = {
            "Nonce": "azhhbtqctwlwafko746e",
	        "ReqTime": "1630479544237",
	        "TerminalType": "Android",
	        "AppID": "10100",
	        "Phone": "18848885959",
	        "Signature": "B8DB15128213EB8E4BEF5C650B29059E",
	        "TerminalVersion": "1.6.9t1",
	        "Password": "EqZbW/HQFJw="
        }
        header = {
            'Accept':'application/json','User-Agent':'okhttp/3.12.0','Content-Type':'application/json'
        }
        url = 'http://butlerapp-test.diyibox.com/User/Login'
        response = requests.post(url=url, headers=header, data=json.dumps(data)
                                 )
        self.assertEqual(response.status_code, 200, '返回状态错误，不为200')
        print(response.text)
        print(response.json()[data], 'ExcuteMsg')

    def test_VerificationAvailable(self):
        data = {
            "Nonce": "rarqqd4592ekv31g691s",
	        "TenantID": "88687809",
	        "ReqTime": "1630477183764",
	        "TerminalType": "Android",
	        "AccountID": "5379",
	        "AppID": "10100",
	        "BelongCompanyId": "88688117",
	        "Signature": "5ABAB404FBA9DA9353C0091F06649F24",
	        "StationId": "88688202",
	        "AccountType": "21",
	        "TerminalVersion": "1.6.9t1"
        }
        header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json', 'accept': 'application/json',
                  'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoie1wiVXNlcklkXCI6NTM3OSxcIlRlbmFudElkXCI6ODg2ODc4MDksXCJTdGF0aW9uSWRcIjpudWxsLFwiU21hcnRCb3hTblwiOm51bGx9IiwibmJmIjoxNjMwNDc3MTgzLCJleHAiOjE2MzEwODE5ODMsImlhdCI6MTYzMDQ3NzE4M30.ymIcVZdnSSjTDefD8URaboCZ1nCeF0PuoMO2uVbyDfE'
        }
        '''
        header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json', 'accept': 'application/json',
                  'authorization': 'Bearer ' + str(Token)}
        '''
        response = requests.post('http://butlerapp-test.diyibox.com/User/VerificationAvailable', data=json.dumps(data),
                                 headers=header)
        self.assertEqual(response.status_code, 200, '返回状态错误，不为200')
        print(response.text)
