import requests
from wxpy import *
import traceback
session = requests.session()
key = "81410c064db0455ca2debf20c5aa9972"
data = {
    'userId': "test111123",
    'question': "天气",
    'type':'1'}
# result = session.post('http://nlp.xiaoi.com/ask.do', data)
# print(result.text)
class Msg():
    def __init__(self):
        self.text = "1+1"
    def reply(self,ret):
        print("小i："+ret)
xiaoi = XiaoI('yHAPUxbItyRT', 'LY1QEhtY3el8TcekBfOY')
msg = Msg()
res = xiaoi.do_reply(msg)


