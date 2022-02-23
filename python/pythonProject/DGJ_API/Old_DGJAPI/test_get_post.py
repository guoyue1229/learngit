import requests

import json

class Runmain:

    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers).json()
        return response
        # return json.dumps(response,sort_keys=True,indent=4)

    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers).json()
        #return response
        return json.dumps(response,sort_keys=True,indent=4)

    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url,params,headers)
        else:
            respose = self.send_post(url,data,headers)
        return respose
if __name__ == '__main__':
        run =Runmain()
        method = 'POST'
        url = "http://butlerapp-gray.diyibox.com/User/Login"
        headers = {
            "User-Agent": "okhttp/3.12.0",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer "
        }
        params = None
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
        response = run.run_main(url,params,jsondata,headers,method)
        print(response)
        print(data)
