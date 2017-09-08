#!/usr/local/bin/python3

import time

num = int(input('有多少组玩家\n'))
guessWord = []
correct = []
# 定义列表，num+10是不想让guessWord下标不合法
for i in range(0, num + 10):
    guessWord.append(0)
    correct.append(0)
wordNum = 10
guessWord[0] = ['打情骂俏', '海绵宝宝', '娇媚', '金鸡独立', '狼吞虎咽', '睡眼朦胧', '鹤立鸡群', '手舞足蹈', '卓别林', '穿越火线']
guessWord[1] = ['眉飞色舞', '英雄联盟', '扭秧歌', '偷看美女', '大摇大摆', '回眸一笑', '市场营销', '大眼瞪小眼', '自恋', '处女座']
guessWord[2] = ['狗急跳墙', '捧腹大笑', '目不转睛', '愁眉苦脸', '左顾右盼', '宫保鸡丁', '升国旗', '暗恋', '臭袜子', '趁火打劫']

flag = 'n'

for i in range(0, num):
    start = time.time()
    for k in range(0, wordNum):
        # 显示词语
        print(('%d.%s') % (k + 1, guessWord[i][k]))

        flag = input('请答题,答对请输入y,跳过请输入任意键')
        end = time.time()
        sec = end - start
        # 统计用时
        if (110 <= sec <= 120):
            print('还有10秒钟')
        if (sec >= 120):
            print('时间到！游戏结束')
            break

        if (flag == 'y'):
            correct[i] = correct[i] + 1
            continue
        else:
            continue
    str_temp = ('第%d组答对数目:%d') % (i + 1, correct[i])
    print(str_temp)
