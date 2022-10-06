# weishao sign in edit info script 
# Statement 声明 
# For learning reference only, please do not use it for illegal purposes, Bear the consequences
# 仅供学习参考，请勿用做非法用途，后果自负

import requests 

# Golbal Variable
# cookie 
cookie = ""
referer = "


# request url
url = "https://yq.weishao.com.cn/api/questionnaire/questionnaire/editAnswer"

# request pack headers
hearder = {
    # Get you application cookie Fill in cookie variable
    "Cookie": cookie,
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Origin": "https://yq.weishao.com.cn",
    "Content-Length": "6820",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 weishao(6.8.16) wsi18n(zh)",
    "Referer": referer,
    "Accept-Encoding": "gzip, deflate"}

# request send payload
# Please use application get your weishao application sent server datapack contant and then place json data in payload
payload = ""

# Program entry
if __name__ == '__main__':
    ret = requests.post(url, headers=hearder,json=payload)
    print(ret.status_code)
    print('\n\n')
    print(ret.text)
