# 获取所有好友和所有群组

from wxpy import *

# 初始化机器人，扫描登录
bot = Bot()

my_friends = bot.friends()
print(my_friends)
my_friend = my_friends.search('陈军')[0]
my_friend.send('000000000000')

my_groups = bot.groups()
print(my_groups)

my_group = my_groups.search('查查吧')[0]
print(my_group)
my_group.send('0000000')


my_chats = bot.chats()
print(my_chats)


