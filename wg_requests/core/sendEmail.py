# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email


class send_email:
    def __init__(self, From, To, Cs, pw, file_path, file_header, file_body, smtp_server='smtp.qq.com'):
        # 发送人
        self.From = From
        # 收件人['aaa@a.com','bbb@a.com']
        self.To = list(To)
        # 抄送人
        self.Cs = list(Cs)
        # 登录邮件密码base64.encodestring('明文')加密后密码
        self.pw = pw
        # 文件具体路径(路径+文件名称)
        self.file_path = file_path
        # 标题头
        self.file_header = file_header
        # 内容
        self.file_body = file_body
        self.smtp_server = smtp_server

    def login(self):
        server = smtplib.SMTP_SSL(self.smtp_server)
        server.connect(self.smtp_server, 465)
        server.login(self.From, self.pw)
        receive = self.To
        receive.extend(self.Cs)
        print('send from:%s\r\n'%self.From+'sendto:%s\r\n'%self.To)
        server.sendmail(self.From, self.To, self.atta())
        print('测试报告已发送至邮箱')
        server.quit()


    def atta(self):
        main_msg = MIMEMultipart()
        # 内容
        text_msg = MIMEText(self.file_body)
        main_msg.attach(text_msg)
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)

        data = open(self.file_path, 'rb')
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.encoders.encode_base64(file_msg)
        basename = os.path.basename(self.file_path.split('/')[-1])
        print(basename)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
        main_msg.attach(file_msg)
        main_msg['From'] = self.From
        main_msg['To'] = ";".join(self.To)
        main_msg['Cs'] = ";".join(self.Cs)

        # 标题头
        main_msg['Subject'] = self.file_header
        main_msg['Date'] = email.utils.formatdate()

        fullText = main_msg.as_string()

        return fullText

# 在runcase页面调send_emial方法
if __name__ == '__main__':
    s = send_email('278920292@qq.com', ['zjyang@jmail.com', '278920292@qq.com'], '',
                   'vycieiwmvsjncagb',
                   'E:\work_soft\PyCharm\PyCharm Community Edition 2017.2.4\project\wangguan\wg_requests\case_unittest\htmlreport' + '/接口测试报告.html', '测试邮件',
                   'test')
    s.login()
