#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: run_method.py
import requests
import json

class RunMethod(object):

    def post_main(self, url, headers, data):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        response = requests.post(url=url, headers=headers, data=data, verify=False)
        '''
        if headers is not None:
            response = requests.post(url=url, data=data, headers=headers, verify=False)
        else:
            response = requests.post(url=url, data=data, verify=False)
        # print("响应码：", response.status_code)
        '''
        return response

    def get_main(self, url, headers, data=None):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=url, headers=headers, data=data, verify=False)
        '''
        if headers is not None:
            response = requests.get(url=url, data=data, headers=headers, verify=False)
        else:
            response = requests.get(url=url, data=data, verify=False)
        '''
        return response

    def run_main(self, method, url, headers, data=None):
        # 忽略不安全的请求警告信息
        requests.packages.urllib3.disable_warnings()
        requests.adapters.DEFAULT_RETRIES = 5
        # s = requests.sessions()
        # s.keep_alive = False  # 关闭多余连接

        if method == "Post":
            res = self.post_main(url, headers, data)
        elif method == "Get":
            res = self.get_main(url, headers, data)
        # 将 Python 对象编码成 JSON 字符串
        #return json.dumps(res, ensure_ascii=False, sort_keys=False, indent=2)
        # 将响应的的数据以字典数据结构和json数据格式返回
        return res.json()


if __name__ == "__main__":
    run = RunMethod()
    method = "Post"
    url = "http://butlerapp-gray.diyibox.com/User/Login"
    headers = {
        "User-Agent": "okhttp/3.12.0",
        "Content-Type": "application/json",
        "Accept" : "application/json",
        "Authorization" : "Bearer "
    }
    data = {
	"Nonce": "8q8emxz6ixpycu0tkv88",
	"ReqTime": "1631091435258",
	"TerminalType": "Android",
	"AppID": "10100",
	"Phone": "18838202811",
	"Signature": "7C222177D5A964E7CF4F9B9DE0145C2F",
	"TerminalVersion": "1.6.9t2",
	"Password": "Lq5GTgx6DfQ="
     }
    jsondata = json.dumps(data)
    #res = run.run_main("Post", url, data, headers)
    response = run.run_main(method, url, headers, jsondata)
    print(type(response))
    print(response)
    print(jsondata)
