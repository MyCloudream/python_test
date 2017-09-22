from wxpy import *

# 初始化机器人，扫描登录
bot = Bot()

# 查找群组
my_group = bot.groups().search('查查吧')[0]
# 创建图灵机器人对象
tuling = Tuling(api_key='1797af4e6ba47a2c32863d6ed13d8681')


# 监听对象，所监听的对象发送了消息，则图灵自己回复。如果不传参数，则监听所有对象。
@bot.register(my_group)
def print_others(msg):
    tuling.do_reply(msg)


# 阻塞线程，程序不结束
embed()
