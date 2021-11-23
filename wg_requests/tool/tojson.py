# coding=utf-8
import re
import json
import requests
from param.parambyjson import OperationJson
from case_unittest.login import TestMathFunc_one


# test=TestMathFunc_one().test_one()
# TestMathFunc_one().test_one()
# top = OperationJson().get_value('login')
# payload = top.get('payload')
# p=json.dumps(payload)
# print(p)
# print(payload)

# 测试test
# test={'message': '{"msg":"method","id":"20","method":"login","params":[{"user":{"username":"liyi"},"password":{"digest":"e1cca85c97a6de76dae6293f2597977afa032dfe4c6182524ead31a221684516","algorithm":"sha-256"}}]}','test1':'111','test2':'3333'}
# test1=json.dumps(test)
# print(test1)
#     print("values:"+i)
# for i in test.values():
# for i in test:
#     print("key:" + i)


# js1 = '{"message":"{\"msg\":\"result\",\"id\":\"19\",\"result\":{\"id\":\"pYhsRfC4rwWT68axS\",\"token\":\"pNUX8HoflMjs--9SpUz2ghsLKY3Do1m_KOj21TnvS-P\",\"tokenExpires\":{\"$date\":1645085898485},\"type\":\"password\"}}","success":true}'
# p = re.compile("(message['\"]?: *['\"])(.+)(['\"],)")
# message = p.search(js1).group(2)
# js2 = p.sub(r"\1\3", js1)
# print(js2)
# print(message)
# jsDict = json.loads(js2)
# jsDict['message'] = json.loads(message)
# print(jsDict)


# # 获取字典数据中的某个值
# def get_target_value(key, dic, tmp_list):
#     """
#     :param key: 目标key值
#     :param dic: JSON数据
#     :param tmp_list: 用于存储获取的数据
#     :return: list
#     """
#     if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
#         return 'argv[1] not an dict or argv[-1] not an list '
#
#     if key in dic.keys():
#         tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
#
#     for value in dic.values():  # 传入数据不符合则对其value值进行遍历
#         if isinstance(value, dict):
#             get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
#         elif isinstance(value, (list, tuple)):
#             _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
#
#     return tmp_list



# 调用自身函数，self.函数（）
# def _get_value(key, val, tmp_list):
#     for val_ in val:
#         if isinstance(val_, dict):
#             get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
#         elif isinstance(val_, (list, tuple)):
#             _get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身
#
#             # 获取字典数据中的某个值
#             def get_target_value(self, key, dic, tmp_list):
#                 """
#                 :param key: 目标key值
#                 :param dic: JSON数据
#                 :param tmp_list: 用于存储获取的数据
#                 :return: list
#                 """
#                 if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
#                     return 'argv[1] not an dict or argv[-1] not an list '
#
#                 if key in dic.keys():
#                     tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
#
#                 for value in dic.values():  # 传入数据不符合则对其value值进行遍历
#                     if isinstance(value, dict):
#                         self.get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
#                     elif isinstance(value, (list, tuple)):
#                         self._get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
#
#                 return tmp_list
#
#             def _get_value(self, key, val, tmp_list):
#                 for val_ in val:
#                     if isinstance(val_, dict):
#                         self.get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
#                     elif isinstance(val_, (list, tuple)):
#                         self._get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身

# # 获取json中包含的所有键（包括嵌套字典）
# key_list = []
# def getJsonKey(json_data):
#     # 递归获取字典中所有key
#     for key in json_data.keys():
#         if type(json_data[key]) == type({}):
#             getJsonKey(json_data[key])
#         key_list.append(key)
#     return key_list





# url = "http://192.168.72.235/api/v1/rooms.upload/GENERAL"
#
#
# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n888\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"C:\\Users\\Administrator\\Desktop\\1.png\"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# payload2={"description": (None, "CES"), 'file': ('1', open(r'E:\work_soft\PyCharm\PyCharm Community Edition 2017.2.4\project\wangguan\wg_requests\1.png', 'rb'), 'image/png')}
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'X-Auth-Token': "vSr9QuUCBLGG3w_ez8L_OImyQXzWuDhk6f7t5NLA_G8",
#     'X-Requested-With': "XMLHttpRequest",
#     'X-User-Id': "WnirorucaKfJgntam",
#     'cache-control': "no-cache",
#     'Postman-Token': "59721aa1-7a16-4f30-bc02-2f27a9eaa03e"
#     }
#
# response = requests.request("POST", url, data=payload2, headers=headers)
#
# print(response.text)