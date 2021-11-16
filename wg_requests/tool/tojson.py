# coding=utf-8
import re
import json
import requests

js1 = '''{
    "data": "{\"message\":\"{\\\"msg\\\":\\\"method\\\",\\\"id\\\":\\\"88\\\",\\\"method\\\":\\\"sendMessage\\\",\\\"params\\\":[{\\\"_id\\\":\\\"') + time + str('\\\",\\\"rid\\\":\\\"WnirorucaKfJgntampYhsRfC4rwWT68axS\\\",\\\"msg\\\":\\\"测试1996\\\"}]}\"}",
    "message": "获取成功！",
    "success": true
}'''
p = re.compile("(data['\"]?: *['\"])(.+)(['\"],)")
data = p.search(js1).group(2)
js2 = p.sub(r"\1\3", js1)
jsDict = json.loads(js2)
jsDict['data'] = json.loads(data)
print(jsDict)





url = "http://192.168.72.235/api/v1/rooms.upload/GENERAL"


payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n888\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"C:\\Users\\Administrator\\Desktop\\1.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
payload2={"description": (None, "CES"), 'file': ('1', open(r'E:\work_soft\PyCharm\PyCharm Community Edition 2017.2.4\project\wangguan\wg_requests\1.png', 'rb'), 'image/png')}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'X-Auth-Token': "vSr9QuUCBLGG3w_ez8L_OImyQXzWuDhk6f7t5NLA_G8",
    'X-Requested-With': "XMLHttpRequest",
    'X-User-Id': "WnirorucaKfJgntam",
    'cache-control': "no-cache",
    'Postman-Token': "59721aa1-7a16-4f30-bc02-2f27a9eaa03e"
    }

response = requests.request("POST", url, data=payload2, headers=headers)

print(response.text)