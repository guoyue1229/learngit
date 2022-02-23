# coding:utf-8
import json
import unittest

import requests

import HTMLFunction
from HTMLFunction import *


class Test(unittest.TestCase):
    Token = None
    header = None
    host = 'https://butlerapp.diyibox.com'
    Express = GetNonce(13).upper()
    Expresss = GetNonce(13).upper()
    Expressss = GetNonce(13).upper()
    Expres = GetNonce(14).upper()

    @classmethod
    # 测试启动
    def setUpClass(cls):
        # 登录获取Token,添加至header防止报Unauthorized
        url = cls.host + '/User/Login'
        header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json', 'accept': 'application/json',
                  'authorization': 'Bearer '}
        data = {
            "ReqTime": GetTime(False),
            "Phone": "17821357652",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "Password": "NS1uJvZWJP4=",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data)
        response = requests.post(url, data=json.dumps(data), headers=header)
        if response.ok is True:
            cls.Token = response.json()["Data"]["Token"]  # 设置Token
            cls.header = {'user-agent': 'okhttp/3.12.0', 'content-type': 'application/json',
                          'accept': 'application/json',
                          'authorization': 'Bearer ' + str(cls.Token)}
        else:
            print('登录失败')
            # 发送邮箱
            return
        # print("类执行之前的方法")

    @classmethod
    # 测试结束
    def tearDownClass(cls):
        # print("类执行之后的方法")
        pass

    # 每次方法前执行
    def setUp(self):
        # self.run = Runmain()
        pass

    # 每次方法后执行
    def tearDown(self):
        pass

    def test_GetVersion(self):
        url = self.host + '/APP/GetVersion'
        data = {
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "TerminalVersion": "1.5.6",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetStationAppAdverList(self):
        url = self.host + '/APP/GetStationAppAdverList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "AdverType": "5",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AdverSite": "101",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SystemNotice(self):
        url = self.host + '/APP/SystemNotice'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_VerificationAvailable(self):
        # 验证余额是否充足
        url = self.host + '/User/VerificationAvailable'
        data = {
            "ReqTime": GetTime(False),
            "BelongCompanyId": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AccountType": "20",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_QueryUserInfo(self):
        url = self.host + '/User/QueryUserInfo'
        data = {
            "ReqTime": GetTime(False),
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetExpressCompany(self):
        url = self.host + '/BasicInfo/GetExpressCompany'
        data = {
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "TerminalVersion": "1.5.6",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetProvinceList(self):
        url = self.host + '/BasicInfo/GetProvinceList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetSyncData(self):
        url = self.host + '/Station/GetSyncData'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_Statistics(self):
        url = self.host + '/SendOrder/Statistics'
        data = {
            "ReqTime": GetTime(20),
            "Type": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "ExpressCompanyId": "-1",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Time": GetTime(),
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_Statistics(self):
        url = self.host + '/V2/SendOrder/Statistics'
        data = {
            "ReqTime": GetTime(False),
            "Type": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "ExpressCompanyId": "-1",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.7.3",
            "AccountID": "8",
            "Time": GetTime(),
            "Signature": "59B93F97A0204D3D570336E17EF82589",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SendOrderSearch(self):
        url = self.host + '/SendOrder/SendOrderSearch'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "LingerStatus": "0",
            "TenantID": "80000002",
            "SmsSendStatus": "0",
            "OrderStatus": "1",
            "ExpressId": "0",
            "Keyword": "",
            "AccountID": "8",
            "TimeType": "0",
            "ExpressInType": "0",
            "TerminalType": "Android",
            "AppID": "0",
            "StartTime": GetTime() + " 00:00:00",
            "EndTime": GetTime() + " 00:00:00",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_SendOrderSearch(self):
        url = self.host + '/V2/SendOrder/SendOrderSearch'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "LingerStatus": "0",
            "TenantID": "80000002",
            "SmsSendStatus": "0",
            "OrderStatus": "1",
            "ExpressId": "0",
            "Keyword": "",
            "AccountID": "8",
            "TimeType": "0",
            "PageSize": "10",
            "ExpressInType": "0",
            "TerminalType": "Android",
            "AppID": "0",
            "StartTime": GetTime() + " 00:00:00",
            "YearMonth": "2020-12",
            "LinePosition": "0",
            "EndTime": GetTime() + " 00:00:00",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.7.3",
            "Signature": "8670195D7B201A84981D9230F31CBF4A"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_QueryBlackList(self):
        url = self.host + '/SendOrder/QueryBlackList'
        data = {
            "ReqTime": GetTime(False),
            "Page": "0",
            "StationId": "2",
            "Size": "0",
            "ExpressNo": "",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_WalletTradeInfo(self):
        url = self.host + '/User/WalletTradeInfo'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_ChangeOperatorAddress(self):
        url = self.host + '/User/ChangeOperatorAddress'
        data = {
            "ReqTime": GetTime(False),
            "OperatorAddress": "123",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_WalletTradeHistory(self):
        url = self.host + '/User/WalletTradeHistory'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0",
            "StartTime": GetTime() + " 00:00:00",
            "Type": "-1",
            "EndTime": GetTime() + " 23:59:59",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_WalletTradeMoney(self):
        url = self.host + '/User/WalletTradeMoney'
        data = {
            "StartTime": GetTime() + " 00:00:00",
            "ReqTime": GetTime(False),
            "Type": "-1",
            "StationId": "2",
            "EndTime": GetTime() + " 23:59:59",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SetAddress(self):
        url = self.host + '/Station/SetAddress'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "AccountID": "8",
            "ProvinceCode": "1087",
            "TerminalType": "Android",
            "AppID": "0",
            "Address": "新业大楼2号楼末端联盟",
            "CityCode": "1375",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AreaCode": "2371",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetStationDetailByAccountId(self):
        url = self.host + '/Station/GetStationDetailByAccountId'
        data = {
            "ReqTime": GetTime(False),
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SetContact(self):
        url = self.host + '/Station/SetContact'
        data = {
            "ReqTime": GetTime(False),
            "Phone": "17821357652",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Name": "钟广安",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SetOpeningTime(self):
        url = self.host + '/Station/SetOpeningTime'
        data = {
            "StartTime": "00:00",
            "ReqTime": GetTime(False),
            "StationId": "2",
            "EndTime": "00:00",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetStationSendFeeList(self):
        url = self.host + '/Station/GetStationSendFeeList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_RemoveDispatchCompany(self):
        url = self.host + '/Station/RemoveDispatchCompany'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Data": [{
                "ExpressCompanyId": 46
            }],
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.6"
        }
        data["Signature"] = "123"
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetStationExpressList(self):
        url = self.host + '/Station/GetStationExpressList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_RemoveExpreeCompany(self):
        url = self.host + '/Station/RemoveExpreeCompany'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Data": [{
                "ExpressCompanyId": 3
            }],
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.6"
        }
        data["Signature"] = "123"
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetCustomerLables(self):
        url = self.host + '/Station/GetCustomerLables'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetCustomerList(self):
        url = self.host + '/Station/GetCustomerList'
        for a in range(1, 3):
            print(a)
            data = {
                "ReqTime": GetTime(False),
                "StationId": "2",
                "LabelId": str(a),
                "TenantID": "80000002",
                "Nonce": GetNonce(20),
                "TerminalVersion": "1.5.6",
                "AccountID": "8",
                "AppID": "0",
                "TerminalType": "Android"
            }
            data["Signature"] = GetSign(data, self.Token)
            response = requests.post(url, data=json.dumps(data),
                                     headers=self.header)
            print(json.dumps(data))
            print(response.text)
            self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_EquipmentList(self):
        url = self.host + '/Station/EquipmentList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddPrintEquipment(self):
        url = self.host + '/Station/AddPrintEquipment'
        data = {
            "ReqTime": GetTime(False),
            "EquipmentNo": "21312312312312",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "EquipmentName": "1231231",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_ExpressInSmartShelf(self):
        url = self.host + '/V2/SendOrder/ExpressInSmartShelf'
        data = {
            "ReqTime": "1607652745532",
            "StationId": "2",
            "Data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Expressss,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "SendOrderId": 0,
                "ShelfNo": "TEST",
                "Time": GetTime(1),
                "Type": "201"
            }],
            "ShelfType": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.7.3",
            "AccountID": "8",
            "Signature": "EB11D5177CEB0F865BED05D357128900",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SelShelfBoxOpen(self):
        url = self.host + '/KernelShelfBox/SelShelfBoxOpen'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SelKernelShelfBoxList(self):
        url = self.host + '/KernelShelfBox/SelKernelShelfBoxList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddKernelShelfBoxList(self):
        url = self.host + '/KernelShelfBox/AddKernelShelfBoxList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "ShelfNo": GetNonce(5).upper(),
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_DelKernelShelfBox(self):
        url = self.host + '/KernelShelfBox/DelKernelShelfBox'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "Id": "0",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetSMSSetList(self):
        url = self.host + '/Station/GetSMSSetList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetSMSSet(self):
        url = self.host + '/Station/GetSMSSet'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SetStationNotify(self):
        url = self.host + '/Station/SetStationNotify'
        data = {
            "StationNotifyType": "2",
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetSmsTemplateTag(self):
        url = self.host + '/SmsTemplate/GetSmsTemplateTag'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetTemplate(self):
        url = self.host + '/SmsTemplate/GetTemplate'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddTemplate(self):
        url = self.host + '/SmsTemplate/AddTemplate'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "BizType": "1",
            "MsgType": "1",
            "Content": "123",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetTemplateList(self):
        url = self.host + '/VoiceTemplate/GetTemplateList'
        data = {
            "ReqTime": GetTime(False),
            "VoiceType": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppealStatus": "1",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetVoiceTemplateTag(self):
        url = self.host + '/VoiceTemplate/GetVoiceTemplateTag'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddTemplate(self):
        url = self.host + '/VoiceTemplate/AddTemplate'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "MsgType": "1",
            "TenantID": "80000002",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0",
            "Content": "[expressnoAll]",
            "BizType": "1",
            "Nonce": GetNonce(20),
            "VoiceTime": "0",
            "TerminalVersion": "1.5.6",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetAppVersionList(self):
        url = self.host + '/APP/GetAppVersionList'
        data = {
            "ReqTime": GetTime(False),
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_UploadSuggest(self):
        url = self.host + '/APP/UploadSuggest'
        data = {
            "ReqTime": GetTime(False),
            "PicUrl": "",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "Suggest": "123",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetIconList(self):
        url = self.host + '/BasicInfo/GetIconList'
        data = {
            "ReqTime": GetTime(False),
            "Type": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetSystemMsgAndAnnounceList(self):
        url = self.host + '/APP/GetSystemMsgAndAnnounceList'
        for a in range(0, 2):
            data = {
                "ReqTime": GetTime(False),
                "Type": str(a),
                "Page": "1",
                "StationId": "2",
                "TenantID": "80000002",
                "Nonce": GetNonce(20),
                "TerminalVersion": "1.5.6",
                "AccountID": "8",
                "AppID": "0",
                "TerminalType": "Android"
            }
            data["Signature"] = GetSign(data, self.Token)
            response = requests.post(url, data=json.dumps(data),
                                     headers=self.header)
            print(json.dumps(data))
            print(response.text)
            self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_Status(self):
        url = self.host + '/SendOrder/Status'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "ExpressNo": self.Express,
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_QueryExpressCompanyByExpressNo(self):
        url = self.host + '/SendOrder/QueryExpressCompanyByExpressNo'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "ExpressNo": self.Express,
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "ExpressInType": "201",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_ExpressInNew(self):
        url = self.host + '/SendOrder/ExpressInNew'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Express,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "ShelfNo": "01A001",
                "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "Type": "201"
            }],
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "Signature": "1F0C5D2F723022D445DFFC7C2EDF05BF",
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.6"
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_ExpressInNew(self):
        url = self.host + '/V2/SendOrder/ExpressInNew'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Expresss,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "ShelfNo": "11A001",
                "Time": GetTime(1),
                "Type": "201"
            }],
            "Nonce": "ivh4p477berngyxsqn6x",
            "ReqTime": GetTime(False),
            "Signature": "4DC00BC263715239FBF75EC159FF5F2A",
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.7.3"
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_Baginformation(self):
        url = self.host + '/SendOrder/Baginformation'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "ExpressCompanyId": "1",
            "Nonce": GetNonce(20),
            "OrderStatus": "3",
            "BagExpressNo": self.Express,
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetNotSignedWaybill(self):
        url = self.host + '/SendOrder/GetNotSignedWaybill'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "ExpressNo": self.Express,
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetJdStationReport(self):
        url = self.host + '/SendOrder/GetJdStationReport'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_Arrive(self):
        url = self.host + '/SendOrder/Arrive'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Nonce": GetNonce(20),
            "Signature": "A8855E6B0FC6D0D1D9FCC6D302976739",
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.6",
            "data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Express,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }]
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_Arrive(self):
        url = self.host + '/V2/SendOrder/Arrive'
        data = {
            "AccountID": "8",
            "AppID": "0",
            "Nonce": GetNonce(20),
            "ReqTime": GetTime(False),
            "Signature": "78CD93BDF00402C16939FF901CADB262",
            "StationId": "2",
            "TenantID": "80000002",
            "TerminalType": "Android",
            "TerminalVersion": "1.5.7.3",
            "data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Express,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "Time": GetTime() + " 09:00:00"
            }]
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_ExpressInSmartShelf(self):
        url = self.host + '/SendOrder/ExpressInSmartShelf'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "Data": [{
                "ArrivePayAmount": "0",
                "ExpressCompanyId": "1",
                "ExpressNo": self.Expres,
                "InsteadPayAmount": "0",
                "ReceiverMobile": "17821357652",
                "SendOrderId": 0,
                "ShelfNo": "123",
                "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "Type": "201"
            }],
            "ShelfType": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Signature": "6512F214A06655257D62CAE68C6460D5",
            "TerminalType": "Android",
            "AppID": "0"
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_ExpressOutNew(self):
        url = self.host + '/SendOrder/ExpressOutNew'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "Data": [{
                "ExpressCompanyId": "1",
                "ExpressNo": self.Express,
                "PhotoStatus": "0",
                "PhotoUrl": "",
                "Remark": "本人签收",
                "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "Type": "301"
            }],
            "TenantID": "80000002",
            "IsOut": "2",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Signature": "57AC8A68EA272E6DF1CA096B2CD70434",
            "TerminalType": "Android",
            "AppID": "0"
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_V2_ExpressOutNew(self):
        url = self.host + '/V2/SendOrder/ExpressOutNew'
        data = {
            "ReqTime": "1607652218958",
            "StationId": "2",
            "Data": [{
                "ExpressCompanyId": "1",
                "ExpressNo": self.Expresss,
                "PhotoStatus": "0",
                "PhotoUrl": "",
                "Remark": "本人签收",
                "Time": GetTime(1),
                "Type": "301"
            }],
            "TenantID": "80000002",
            "IsOut": "2",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.7.3",
            "AccountID": "8",
            "Signature": "6E5F118909A72EE1262385C5B9610176",
            "TerminalType": "Android",
            "AppID": "0"
        }
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_MsgResendList(self):
        url = self.host + '/SendOrder/MsgResendList'
        data = {
            "ReqTime": GetTime(False),
            "MsgSendStatus": "4",
            "Page": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Keyword": "",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0",
            "ExpressInType": "-1",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_StatisticsOrder(self):
        url = self.host + '/PostOrder/StatisticsOrder'
        data = {
            "ReqTime": GetTime(False),
            "Type": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "ExpressCompanyId": "-1",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "Time": GetTime(),
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_StationSearchOrder(self):
        url = self.host + '/PostOrder/StationSearchOrder'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "CompleteStatus": "0",
            "TenantID": "80000002",
            "Keyword": "",
            "AccountID": "8",
            "OrderType": "1",
            "TerminalType": "Android",
            "AppID": "0",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_PostOrderUrl(self):
        url = self.host + '/PostOrder/PostOrderUrl'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetStationIsOpenPostMustWeigh(self):
        url = self.host + '/Station/GetStationIsOpenPostMustWeigh'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddressBookList(self):
        url = self.host + '/PostOrder/AddressBookList'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "Keyword": "",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_CalcOrderAmout(self):
        url = self.host + '/PostOrder/CalcOrderAmout'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "ProvinceId": "1087",
            "Weight": "1000",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0",
            "Nonce": GetNonce(20),
            "ExpressCompanyId": "1",
            "TerminalVersion": "1.5.6",
            "SenderMobile": "17821357652",
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_AddOrderElectronic(self):
        url = self.host + '/PostOrder/AddOrderElectronic'
        data = {
            "ReceiverName": "林俊杰",
            "StationId": "2",
            "DiscountAmount": "0.0",
            "TenantID": "80000002",
            "PremiumFee": "0.0",
            "ProductName": "包裹",
            "AccountID": "8",
            "PayWay": "1",
            "SenderAreaId": "2371",
            "SenderName": "钟广安",
            "TerminalVersion": "1.5.6",
            "ReqTime": GetTime(False),
            "ReceiverAddress": "林俊杰",
            "Weight": "1000",
            "ReceiverCityId": "1375",
            "SenderCityId": "1375",
            "AppID": "0",
            "TerminalType": "Android",
            "PackageFee": "0.0",
            "ReceiverProvinceId": "1087",
            "ReceiverAreaId": "2371",
            "ReceiverMobile": "17821357652",
            "Amount": "0.0",
            "SenderAddress": "田林路398号新业大楼2号楼",
            "SenderProvinceId": "1087",
            "ExpressCompanyId": "1",
            "Nonce": GetNonce(20),
            "SenderMobile": "17821357652",
            "SenderIdCardNo": "360302196912033023"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')
        HTMLFunction.ExcuteMsg = response.json()["Data"]["ExcuteMsg"]

    def test_StationOrderDetail(self):
        url = self.host + '/PostOrder/StationOrderDetail'
        data = {
            "ReqTime": "1606801223502",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": "7spw0cq1c32xdyd7169a",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "PostOrderId": str(HTMLFunction.ExcuteMsg),
            "Signature": "C07A0C9A9D075CA001C087F73EB753D3",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_EditIosDetails(self):
        url = self.host + '/PostOrder/EditIosDetails'
        data = {
            "ReceiverName": "林俊杰",
            "StationId": "2",
            "DiscountAmount": "0.00",
            "TenantID": "80000002",
            "PremiumFee": "0.00",
            "ProductName": "包裹",
            "AccountID": "8",
            "SenderAreaId": "2371",
            "SenderName": "钟广安",
            "TerminalVersion": "1.5.6",
            "ReqTime": GetTime(False),
            "ReceiverAddress": "林俊杰",
            "ReceiveCode": "",
            "Weight": "1000",
            "ReceiverCityId": "1375",
            "SenderCityId": "1375",
            "PostOrderId": str(HTMLFunction.ExcuteMsg),
            "AppID": "0",
            "TerminalType": "Android",
            "PackageFee": "0.00",
            "ReceiverProvinceId": "1087",
            "ReceiverAreaId": "2371",
            "Amount": "0.00",
            "ReceiverMobile": "17821357652",
            "SenderAddress": "田林路398号新业大楼2号楼",
            "Nonce": GetNonce(20),
            "SenderProvinceId": "1087",
            "ExpressCompanyId": "1",
            "SenderMobile": "17821357652",
            "SenderIdCardNo": "360302196912033023"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_ProduceExpressNo(self):
        url = self.host + '/PostOrder/ProduceExpressNo'
        data = {
            "ReqTime": GetTime(False),
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "PostOrderId": str(HTMLFunction.ExcuteMsg),
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_SearchSuffix(self):
        url = self.host + '/SendOrder/SearchSuffix'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "Keyword": "17821353752",
            "TerminalVersion": "1.5.6",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_StatisticsList(self):
        url = self.host + '/SendOrder/StatisticsList'
        for a in range(1, 9):
            data = {
                "ReqTime": GetTime(False),
                "Page": "1",
                "StationId": "2",
                "TenantID": "80000002",
                "AccountID": "8",
                "TerminalType": "Android",
                "AppID": "0",
                "SendOrderType": str(a),
                "Type": "1",
                "Nonce": GetNonce(20),
                "ExpressCompanyId": "-1",
                "TerminalVersion": "1.5.6",
                "Time": "2020-12-01",
            }
            data["Signature"] = GetSign(data, self.Token)
            response = requests.post(url, data=json.dumps(data),
                                     headers=self.header)
            print(json.dumps(data))
            print(response.text)
            self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_StatisticsStatusList(self):
        url = self.host + '/SendOrder/StatisticsStatusList'
        data = {
            "ReqTime": GetTime(False),
            "Page": "1",
            "StationId": "2",
            "TenantID": "80000002",
            "AccountID": "8",
            "TerminalType": "Android",
            "AppID": "0",
            "SendOrderType": "1",
            "Type": "1",
            "Nonce": GetNonce(20),
            "ExpressCompanyId": "-1",
            "TerminalVersion": "1.5.6",
            "Time": GetTime(),
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')

    def test_GetQiniuToken(self):
        url = self.host + '/BasicInfo/GetQiniuToken'
        data = {
            "ReqTime": GetTime(False),
            "Type": "3",
            "StationId": "2",
            "TenantID": "80000002",
            "Nonce": GetNonce(20),
            "TerminalVersion": "1.5.7.3",
            "AccountID": "8",
            "Signature": "1FE235CBAF175E64612F7C87EB61D300",
            "FileKey": "OutWarehouseQiNiuToken.jpg",
            "AppID": "0",
            "TerminalType": "Android"
        }
        data["Signature"] = GetSign(data, self.Token)
        response = requests.post(url, data=json.dumps(data),
                                 headers=self.header)
        print(json.dumps(data))
        print(response.text)
        self.assertEqual(response.json()["Code"], 200, '返回状态错误，不为200')
