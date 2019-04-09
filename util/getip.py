import requests
import socket
import urllib
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def get_ip(ip):
    my_sender = '*********'  # 发件人邮箱账号
    my_pass = '###########'  # 发件人stamp
    my_user   = '*******'  # 收件人邮箱账号，我这边发送给自己

    def mail():
        ret = True
        try:
            msg = MIMEText(ip, 'plain', 'utf-8')
            msg['From'] = formataddr(["优秀社会主义接班人", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["ip", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "我的ip"  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:
            ret = False
            print(e)
        return ret

    ret = mail()
    if ret:
        print("|--------------------------------------------------------------------|")
        print("|                      邮件发送成功                                  |")
        print("|                   好嗨哟 你可以关闭了                              |")
        print("|--------------------------------------------------------------------|")
    else:
        print("|--------------------------------------------------------------------|")
        print("|                      邮件发送失败                                  |")
        print("|                   请联系 坑坑  QQ：1452245133                     |")
        print("|--------------------------------------------------------------------|")

if __name__ == '__main__':

     ip = get_host_ip()
     get_ip(ip)
