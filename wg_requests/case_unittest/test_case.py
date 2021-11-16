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
import os

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


class TestMathFunc_one(unittest.TestCase):
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

    def test_one(self):
        # 路由
        uri = '/api/v1/method.callAnon/login'
        comm = Common('http://192.168.72.235', api_type='http')
        payload = "{\"message\":\"{\\\"msg\\\":\\\"method\\\",\\\"id\\\":\\\"19\\\",\\\"method\\\":\\\"login\\\",\\\"params\\\":[{\\\"user\\\":{\\\"username\\\":\\\"yangzijian\\\"},\\\"password\\\":{\\\"digest\\\":\\\"312433c28349f63c4f387953ff337046e794bea0f9b9ebfcb08e90046ded9c76\\\",\\\"algorithm\\\":\\\"sha-256\\\"}}]}\"}"
        headers = {
            "Content-Type": "application/json",
            "cache-control": "no-cache",
            "Postman-Token": "9acc4fd3-635b-460d-a4c5-bbc3df510d4b"
        }
        response_selectEq = comm.post(uri, params=payload,headers=headers)
        response_result=response_selectEq.text
        result = str(json.loads(response_selectEq.text).get('success'))
        res = 'True'
        final=res==result
        print(response_result)
        print(result)
        # response_result.append(result)

        self.assertEqual(True, final, '不通过')

    # @unittest.skip("i don't want to run this case")
    # def test_minus(self):
    #     """Test method minus(a,b)"""
    #     self.assertEqual(1,minus(3,2))
    # 
    # def test_multi(self):
    #     """Test method multi(a,b)"""
    #     self.assertEqual(6,multi(2,3))
    # 
    # def test_divide(self):
    #     """Test method divide(a,b)"""
    #     self.assertEqual(2,divide(6,3))
    #     self.assertEqual(2,divide(5, 2))

# 直接运行该文件，测试脚本是否能够运行
if __name__ =='__main__':
    unittest.main()

