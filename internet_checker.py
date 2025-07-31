import requests
import base64
import time
import socket

s = requests.session()

def fun():
    try:
        url = "http://192.168.0.1/goform/goform_set_cmd_process"
        headers = {
             "Referer": "http://192.168.0.1/index.html",
             "User-Agent": "Mozilla/5.0"
        }
        pas = "YWRtaW4="
        payload = {
            "isTest": "false",
            "goformId": "LOGIN",
            "password": pas
         }

        req = s.post(url, data=payload, headers=headers)
        print(req.text)

        reboot_payload = {
             "isTest": "false",
             "goformId": "REBOOT_DEVICE"
        }

        req2 = s.post(url, data=reboot_payload, headers=headers)
        print(req2.text)
    except:
        print('there is error in connection')
        time.sleep(45)
        fun()
def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

# حلقة لا نهائية تفحص الاتصال كل 10 دقائق
while True:
    if not check_internet():
        fun()
    time.sleep(600)  
   


