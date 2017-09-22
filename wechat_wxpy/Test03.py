from wxpy import *

# 初始化机器人，扫描登录
bot = Bot()


@bot.register()
def print_others(msg):
    print(msg)
    my_group = bot.groups().search('查查吧')[0]
    my_group.send(msg)


embed()
