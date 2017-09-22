from wxpy import *

# 初始化机器人，扫描登录
bot = Bot()
bot.self.add()
bot.self.accept()
bot.self.send('能收到吗？')
# 查找好友
# my_friend = bot.friends().search('耿小泰', sex=MALE)[0]
# print(my_friend)


# my_friend.send('hello ')
# my_friend.send_image('C:\\Users\\chenjun\Desktop\\slt17.png')


# @bot.register()
# def print_others(msg):
#     print(msg)

# 自动回复
# 回复 my_friend 的消息 (优先匹配后注册的函数!)
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type)


embed()
