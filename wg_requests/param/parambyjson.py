# coding=utf-8

import json
import os
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
            self.file_name=r'E:\work_soft\PyCharm\PyCharm Community Edition 2017.2.4\project\wangguan\wg_requests\param\api_interface_file\main_s.json'
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
