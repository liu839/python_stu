import easygui as g
import random
titile='猜数字'
secret = random.randint(1,10)
g.msgbox("欢迎玩我设计的小游戏")

guess=g.integerbox(msg='不妨猜一下小甲鱼下现在心里想的是哪个数字')

while guess != secret:

    if guess == secret:
        g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
        g.msgbox("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            g.msgbox("哥，大了大了~~~")
            guess =g.integerbox(msg='不妨再猜一下小甲鱼下现在心里想的是哪个数字')
        else:
            g.msgbox("嘿，小了，小了~~~")
            guess =g.integerbox(msg='不妨再猜一下小甲鱼下现在心里想的是哪个数字')
g.msgbox("游戏结束，不玩啦^_^")
