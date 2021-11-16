# coding=utf-8
'''
Created on 2019-12-10
@author: Zio
'''
import unittest
import sys
sys.path.append(r'C:\work_soft\PyCharm\PycharmProjects\request\untitled')
from core.common import Common
from param.param_openpyxl import ParamFactory
from param.parambyjson import OperationJson
import os
import time
import datetime

import json

# curPath = r'E:\work_soft\PyCharm\PyCharm Community Edition 2017.2.4\project\wangguan\wg_requests\param\api_interface_file'
# searchparamfile = curPath + '/equipmentid_param.xlsx'
# # 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
# searchparam_dict = ParamFactory().chooseParam('xlsx',
#                                               {'file': searchparamfile, 'sheet': 0}).paramAlllineDict()
# print(searchparam_dict)
# 获取当前路径绝对值
        # curPath = os.path.abspath('.')
        # 定义存储参数的excel文件路径

        # i = 0
        # response_result = []
        # exp_list = []
        # while i < len(self.getallcontents().searchparam_dict):
        #     # 读取通过参数类获取的第i行的参数
        #     payload = 'equipmentid=' + str(searchparam_dict[i]['equipmentid'])
        #     # 读取通过参数类获取的第i行的预期
        #     exp = searchparam_dict[i]['exp']
        #     exp_list.append(exp)
        # 
        #     # 进行接口测试
        #     response_selectEq = comm.post(uri_selectEq, params=payload)
        #     # response_result=response_selectEq.text
        #     result = json.loads(response_selectEq.text).get('Message')
        #     response_result.append(result)
        #     # 打印返回结果
        #     print('Response内容：' + response_selectEq.text)
        #     # 读取下一行excel中的数据
        #     i = i + 1
        # print(response_result)
        # print(exp_list)


class TestMathFunc_two(unittest.TestCase):
    """Test mathfunc.py"""

# 每次执行case前后都执行了一次
#     def setUp(self):
#         print ("do something before test.Prepare environment.")
# 
#     def tearDown(self):
#         print ("do something after test.Clean up.")

# setUpClass以及tearDownClass均只执行了一次

    @classmethod
    def setUpClass(cls):
        print("setUp() just one")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() just one")

    # def test_one(self):
    #     top=OperationJson().get_value('login')
    #     payload_messages=top.get('payload')
    #     headers_messages=top.get('headers')
    #     # 路由
    #     uri_selectEq = '/api/v1/method.callAnon/login'
    #     comm = Common('http://192.168.72.235', api_type='http')
    #     payload = payload_messages
    #     headers = headers_messages
    #     response_selectEq = comm.post(uri_selectEq, params=payload,headers=headers)
    #     response_result=response_selectEq.text
    #     result = str(json.loads(response_selectEq.text).get('success'))
    #     res='True'
    #     final=res==result
    #     print(response_result)
    #     print(result)
    #     # response_result.append(result)
    #
    #     self.assertEqual(True,final,'不通过')

    def test_seconds(self):
        top = OperationJson().get_value('loadHistory')
        payload_messages = top.get('payload')
        headers_messages = top.get('headers')
        # 路由
        uri = '/api/v1/method.call/loadHistory'
        comm = Common('http://192.168.72.235', api_type='http')
        payload = payload_messages
        headers = headers_messages
        response_selectEq = comm.post(uri, params=payload, headers=headers)
        response_result = response_selectEq.text
        result = str(json.loads(response_selectEq.text).get('success'))
        res = 'True'
        final = res == result
        print(response_result)
        print(result)
        # response_result.append(result)

        self.assertEqual(True, final, '不通过')

    def test_third(self):
        top = OperationJson().get_value('search')
        payload_messages = top.get('payload')
        headers_messages = top.get('headers')
        # 路由
        uri = '/api/v1/method.call/rocketchatSearch.search'
        comm = Common('http://192.168.72.235', api_type='http')
        payload = payload_messages
        headers = headers_messages
        response_selectEq = comm.post(uri, params=payload, headers=headers)
        response_result = response_selectEq.text
        result = str(json.loads(response_selectEq.text).get('success'))
        res = 'True'
        final = res == result
        print(response_result)
        print(result)
        # response_result.append(result)

        self.assertEqual(True, final, '不通过')

    def test_four(self):
        # 实例化OperationJson()
        opjson=OperationJson()
        data=OperationJson().get_data()
        # id为随机数才可以发消息，这里使用时间戳作为变量，然后修改json文件原本的值
        time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        data['sendMessage'] ['payload'] = str('{\"message\":\"{\\\"msg\\\":\\\"method\\\",\\\"id\\\":\\\"88\\\",\\\"method\\\":\\\"sendMessage\\\",\\\"params\\\":[{\\\"_id\\\":\\\"') + time + str('\\\",\\\"rid\\\":\\\"WnirorucaKfJgntampYhsRfC4rwWT68axS\\\",\\\"msg\\\":\\\"测试1996\\\"}]}\"}')
        # 传入参数给change_value()
        opjson.change_value(data)
        top = OperationJson().get_value('sendMessage')
        payload_messages = top.get('payload')
        headers_messages = top.get('headers')
        # 路由
        uri = '/api/v1/method.call/sendMessage'
        comm = Common('http://192.168.72.235', api_type='http')
        payload = payload_messages
        headers = headers_messages
        response_selectEq = comm.post(uri, params=payload, headers=headers)
        response_result = response_selectEq.text
        result = str(json.loads(response_selectEq.text).get('success'))
        res = 'True'
        final = res == result
        print(response_result)
        print(result)
        # response_result.append(result)

        self.assertEqual(True, final, '不通过')


    def test_five(self):
        top = OperationJson().get_value('sendMessage_image')
        payload_messages = top.get('payload')
        headers_messages = top.get('headers')
        # 路由
        uri = '/api/v1/rooms.upload/GENERAL'
        comm = Common('http://192.168.72.235', api_type='http')
        payload = payload_messages
        print(payload)
        headers = headers_messages
        response_selectEq = comm.post(uri, params=payload, headers=headers)
        response_result = response_selectEq.text



        result = str(json.loads(response_selectEq.text).get('success'))
        res = 'True'
        final = res == result
        print(response_result)
        print(result)
        # response_result.append(result)

        self.assertEqual(True, final, '不通过')


    # @unittest.skip("i don't want to run this case")
    # def test_minus(self):
    #     """Test method minus(a,b)"""
    #     self.assertEqual(1,minus(3,2))



# 直接运行该文件，测试脚本是否能够运行
if __name__ =='__main__':
    unittest.main()

