# -*- coding:utf-8 -*-
"""
娃娃机
======
商场门口有两台娃娃机。兔兔机里有 5 只兔子，抓一次要 2 个币；小熊机里有 8 只小熊，抓一次要 3 个币。

每台机器都要记住五样东西：叫什么、还剩几只娃娃、抓一次要几个币、现在余几个币、已经抓了几次。
两台机器要各记各的：在兔兔机上投币、抓娃娃，小熊机的余币和次数不能跟着变。
所以先写一个类 ClawMachine，说清「一台娃娃机」有哪些数据、会做哪些事，再照着它造出两台机器。

抓一次怎么算：
    余币不够这一台的价钱，就不抓，告诉玩家还差几个币。
    余币够，就先扣掉价钱，已抓次数加 1。
    已抓次数是 3 的倍数（第 3 次、第 6 次……）时必中一只，娃娃少 1 只；其他时候没抓到。

运行后应看到：

    兔兔机投币后余币：7
    第1次：差一点，没抓到
    第2次：差一点，没抓到
    第3次：抓中了！还剩 4 只
    第4次：币不够，还差 1 个
    小熊机投币后余币：9
    第1次：差一点，没抓到
    第2次：差一点，没抓到
    第3次：抓中了！还剩 7 只
    兔兔机：娃娃 4 只，余币 1 个，抓了 3 次
    小熊机：娃娃 7 只，余币 0 个，抓了 3 次

兔兔机抓第 4 次时只剩 1 个币，不够 2 个，所以没抓。
小熊机也抓了 3 次，兔兔机的次数还是 3，两台互不影响。

类清单（名字照写）：
ClawMachine
    __init__(self, name, dolls, price)
        造机器时传进来名字、娃娃数、一次几个币，存成 self.name、self.dolls、self.price。
        余币 self.coins 和已抓次数 self.tries 不用传，一开始都是 0。
    insert(self, n)
        投 n 个币：self.coins 加上 n。return 投完以后的余币。
    status(self)
        return「兔兔机：娃娃 4 只，余币 1 个，抓了 3 次」这样一句。
    grab(self)
        按上面「抓一次怎么算」抓一次。return 这一次的结果，三种句子照样例写。

要求：
1. 类写在最上面，造机器、投币、抓娃娃、打印写在类的下面。
2. 类里每个方法的第一个参数都是 self。调用时不用传 self：
   rabbit.insert(7) 里，Python 把 rabbit 交给 self，把 7 交给 n。
3. 要让机器记住的东西，都写成 self.xxx。只写 coins = 0，出了 __init__ 就没有了。
4. 方法里用 return 交出结果，不要 print。打印都写在下面。
5. 兔兔机写成 ClawMachine("兔兔机", 5, 2)，小熊机写成 ClawMachine("小熊机", 8, 3)。
6. 兔兔机投 7 个币，用 for 连抓 4 次；小熊机投 9 个币，连抓 3 次；最后打印两台的 status()。
   投币那一行写成 print("兔兔机投币后余币：" + str(rabbit.insert(7)))。
   抓的那一行写成 "第" + str(i + 1) + "次：" + rabbit.grab()。
"""
# TODO ① 写 class ClawMachine 和 __init__：名字、娃娃数、价钱从参数来，余币和次数从 0 开始
class ClawMachine:
    def __init__(self, name, dolls, price):
        self.name = name
        self.dolls = dolls
        self.price = price
        self.coins = 0
        self.tries = 0

    def insert(self, n):
        self.coins += n
        return self.coins

    def status(self):
        return (str(self.name)+":娃娃"+str(self.dolls)+"只，余币"+
                str(self.coins)+"个，抓了"+str(self.tries)+"次")

    def grab(self):
        if self.coins < self.price:
            return "第"+str(self.tries)+"次后币不够，还差"+str(self.coins)+"个"
        self.coins -= self.price
        self.tries += 1
        self.dolls -=1
        if self.tries % 3 == 0:
            return "第"+str(self.tries)+"次抓中了！还剩"+str(self.dolls)+"只"
        return "第"+str(self.tries)+"次还差一点，没抓到"

rabbit = ClawMachine("兔兔", 5, 2)
bear = ClawMachine("小熊机", 8, 3)



# TODO ② 写 insert 和 status
#        接着写在 class ClawMachine 里面，缩进 4 格


# TODO ③ 写 grab：先看币够不够；够就扣币、次数加 1；次数是 3 的倍数时必中一只
#        接着写在 class ClawMachine 里面，缩进 4 格


# TODO ④ 造兔兔机和小熊机，投币、抓娃娃，最后打印两台的 status()
print("投币后余币:"+str(rabbit.insert(7)))
for i in range(4):
    print(rabbit.grab())

print("投币后余币:"+str(bear.insert(9)))
for i in range(4):
    print(bear.grab())

print("兔兔机抓取概况："+rabbit.status())
print("小熊机抓取概况："+bear.status())