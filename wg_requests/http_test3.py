
#引入Common、ParamFactory类
from common import Common
from param_openpyxl import ParamFactory
import os
import json

class Public(object):
    """
        说明：
            提供一些常用功能
            1. readExcel():
                读取Excel单元格数据
            2. writeExcel
                写入Excel单元格数据
            3. readCsv():
                读取Csv单元格数据
            4. writeCsv()
                写入Csv单元格数据
            5. getFileCoding()
                获取文件的编码格式
        """

# 获取当前路径绝对值
# curPath = os.path.abspath('.')
# 定义存储参数的excel文件路径
curPath=r'C:\work_soft\PyCharm\equipmentid_param.xlsx'
# searchparamfile = curPath+'/equipmentid_param.xlsx'
searchparamfile = curPath
# 调用参数类完成参数读取，返回是一个字典，包含全部的excel数据除去excel的第一行表头说明
searchparam_dict = ParamFactory().chooseParam('xlsx',{'file':searchparamfile,'sheet':0}).paramAlllineDict()
print(searchparam_dict)
i=0
response_result=[]
exp_list=[]
while i<len(searchparam_dict):
# 读取通过参数类获取的第i行的参数
    payload = 'equipmentid=' + str(searchparam_dict[i]['equipmentid'])
# 读取通过参数类获取的第i行的预期
    exp=searchparam_dict[i]['exp']
    exp_list.append(exp)

# 进行接口测试
    response_selectEq = comm.post(uri_selectEq,params=payload)
    # response_result=response_selectEq.text
    result=json.loads(response_selectEq.text).get('Message')
    response_result.append(result)
# 打印返回结果
    print('Response内容：' + response_selectEq.text)
# 读取下一行excel中的数据
    i=i+1
print(response_result)
print(exp_list)