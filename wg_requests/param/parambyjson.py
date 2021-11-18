# coding=utf-8

import json
# import os

# import os
# import sys
# curPath = os.path.abspath(os.path.dirname(__file__)) #获取当前绝对路径
# filePath = os.path.split(curPath)[0] #获取当前目录的上一级目录路径，将文件名和路径切割，然后只取路径
# sys.path.append(curPath.split('xxxx')[0])#以xxxx来分割，且只取第一个，并把它追加到python系统模块中
# rootPath = curPath.split('xxxx')[0]+"xxxx"#按xxxx分割后，取第一个后，在接上xxxx
# sys.path.append(filePath)#sys.path是python的搜索模块的路径集
# sys.path.append(rootPath)


import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootpath=curPath
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
print(rootpath)

import datetime

class OperationJson:
    '''
    实现读取json文件
    获取json文件内容
    关闭json文件
    读取内容中对应的key、value

    '''
    def __init__(self,file_name=None):
        if file_name:
            self.file_name=file_name
        else:
            self.file_name=rootpath+r'\api_interface_file\main_s.json'
            print(self.file_name)
        self.data = self.get_data()

    # 打开json文件，要加编码规则utf-8
    def get_data(self):
        openfile=open(self.file_name,encoding='utf-8')
        data=json.load(openfile)
        openfile.close()
        # print(data)
        return data

    # 得到顶级父辈机构
    def get_value(self,id):
        return self.data[id]

    def change_value(self,data):
        # time=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # self.data['sendMessage']['payload'] = str('{\"message\":\"{\\\"msg\\\":\\\"method\\\",\\\"id\\\":\\\"88\\\",\\\"method\\\":\\\"sendMessage\\\",\\\"params\\\":[{\\\"_id\\\":\\\"')+time+str('\\\",\\\"rid\\\":\\\"WnirorucaKfJgntampYhsRfC4rwWT68axS\\\",\\\"msg\\\":\\\"测试999\\\"}]}\"}')
        with open(self.file_name, 'w+',encoding='utf-8') as fw:
            json.dump(data, fw, ensure_ascii=False, indent=4)


if __name__=='__main__':
    opr=OperationJson()
    all=opr.get_value('sendMessage')
    print(all)
    # 直接用get方法取字典里的值
    headers_messges=all.get('payload')
