import os
import sys
import requests
import json
from pprint import pprint

client_id = "8P0SXgaX_4aF58IVvzQf"
client_secret = "72WhKq3QnA"

url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity"  # 유명인 얼굴인식

files = {'image': open('irin2.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id,
           'X-Naver-Client-Secret': client_secret}
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode == 200):
    face = json.loads(response.text)
    pprint(face)
else:
    print("Error Code:" + rescode)
