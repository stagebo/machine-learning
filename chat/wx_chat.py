#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wxpy import *
import requests
import traceback

reply = False
key = "81410c064db0455ca2debf20c5aa9972"
session = requests.session()
bot = Bot(console_qr=1)
tuling = Tuling(api_key=key)

fri = bot.friends()
groups = bot.groups()

g = groups.search("坚强")[0]
reply_list = {}
# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    try:
        deal_ret(msg)
    except:
        traceback.print_exc()
@bot.register(fri)
def reply_friend(msg):
    # tuling.do_reply(msg)
    # return
    try:
        deal_ret(msg)
    except:
        traceback.print_exc()


err_code = {
    40001:'参数key错误',
    40002:'请求内容info为空',
    40004:'当天请求次数已使用完',
    40007:'数据格式异常',
}
def deal_ret(msg):
    global  reply
    # if msg.sender.nick_name == "Mr.One":
    if msg.text == "start":
        reply = True
        reply_list[msg.sender.nick_name] = True
        return "开始聊天"
    elif msg.text == "stop":
        reply = False
        reply_list[msg.sender.nick_name] = False
        return "结束聊天"
    reply = reply_list.get(msg.sender.nick_name,False)
    if not reply:
        return

    tuling.do_reply(msg)
    # data = {
    #     'key': key,
    #     'info': msg.text,
    #     'loc':'天津市',
    #     'userid':msg.sender.nick_name
    # }
    # result = session.post('http://www.tuling123.com/openapi/api', {'key': key, 'info': msg.text})
    # ret = result.json()
    # code = ret['code']
    # text = ret['text']
    #
    # ret_msg = ''
    # if code < 40008:
    #     ret_msg = err_code[code]
    # elif code == 100000:
    #     ret_msg = text
    # elif code == 200000:
    #     ret_msg = text + ret['url']
    # elif code >300000:
    #     ret_msg = text
    #     for item in ret['list']:
    #         ret_msg += str(item)
    #
    # return ret_msg


#
# @bot.register(g, TEXT,except_self=False)
# def print_group_msg(msg):
#     if msg.is_at:
#         print(msg)
#         msg.reply(msg.text)

# embed()
bot.join()