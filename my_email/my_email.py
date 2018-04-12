# coding=utf-8
import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
msg_from = 'xxxx@qq.com'  # 发送方邮箱
passwd = 'xxxxxxxxxxxxxx'  # 填入发送方邮箱的授权码
msg_to = 'xxxx@qq.com'  # 收件人邮箱

subject = "python邮件测试"  # 主题
msg = MIMEMultipart('related')
content =  MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')# 正文
# msg = MIMEText(content)
msg.attach(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

file = open("../chat/QR.png", "rb")
img_data = file.read()
file.close()

img = MIMEImage(img_data)
img.add_header('Content-ID', 'imageid')
msg.attach(img)

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print
    "发送成功"
except:
    print( "发送失败")
finally:
    s.quit()