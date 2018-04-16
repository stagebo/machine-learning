#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wxpy import *
import requests
import traceback
import datetime
import send_qr
import threading
key = "81410c064db0455ca2debf20c5aa9972"
# session = requests.session()
# ta = threading.Thread(target=send_qr.send)      #创建一个线程ta，执行 threadfun()
# ta.start()

bot = Bot(qr_callback=send_qr.send)


tuling = Tuling(api_key=key)
# xiaoi = XiaoI('yHAPUxbItyRT', 'LY1QEhtY3el8TcekBfOY')
# 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
group_receiver = ensure_one(bot.groups().search('微信日志'))
# 指定这个群为接收者
logger = get_wechat_logger(group_receiver)

logger.error('程序启动，测试日志...')

fri = bot.friends()
groups = bot.groups()

# g = groups.search("坚强")[0]
reply_list = {}
# qiang = ensure_one(fri.search("强"))

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    # words = 'can you catch what i have say.'
    # sent = list()
    # for i in words:
    #     sen = qiang.send(i)  # 逐字发送
    #     sen.recall()  # 全部撤回

    try:
        deal_ret(msg)
    except:
        logger.error('收到异常信息：'+msg.sender.nick_name+","+msg.text)
        traceback.print_exc()
@bot.register(fri)
def reply_friend(msg):
    try:
        deal_ret(msg)
    except:
        logger.error('收到异常信息：' + msg.sender.nick_name + "," + msg.text)
        traceback.print_exc()


ms = None
def deal_ret(msg):
    global ms
    ms =msg
    # if msg.sender.nick_name == "Mr.One":
    # logger.error(str(datetime.datetime.now())+"-"+msg.sender.nick_name + ": "+msg.text)
    if msg.text.upper().strip()  == "START":
        logger.error(msg.sender.nick_name+"开始了聊天")
        reply_list[msg.sender.nick_name] = True
        logger.error("当前在线情况：" + str(reply_list))
    elif msg.text.upper().strip()  == "STOP":
        logger.error(msg.sender.nick_name + "结束了聊天")
        reply_list[msg.sender.nick_name] = False
        logger.error("当前在线情况：" + str(reply_list))
    reply = reply_list.get(msg.sender.nick_name,False)
    if  reply:
        tuling.do_reply(msg)


embed()
# bot.join()