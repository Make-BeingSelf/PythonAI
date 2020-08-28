
# -*- encoding: utf-8 -*-
import os
import sys
import urllib.request
import json
from pprint import pprint
client_id = "8P0SXgaX_4aF58IVvzQf"  # 개발자센터에서 발급받은 Client ID 값
client_secret = "72WhKq3QnA"  # 개발자센터에서 발급받은 Client Secret 값
#txt = str(input('Trans'))
with open('index.txt', 'r', encoding='utf8') as f:
    resText = f.read()
encText = urllib.parse.quote(resText)
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    res = json.loads(response_body.decode('utf-8'))
    pprint(res)
    with open('trans.txt', 'w', encoding='utf-8') as f:
        f.write(res['message']['result']['translatedText'])
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
