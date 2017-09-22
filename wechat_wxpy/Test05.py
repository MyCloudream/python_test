from wxpy import *
import os
# 初始化机器人，扫描登录
bot = Bot()


# 监听对象，所监听的对象发送了消息，则图灵自己回复。如果不传参数，则监听所有对象。
@bot.register()
def print_others(msg):
    os.system('ping www.baidu.com')


# 阻塞线程，程序不结束
embed()
