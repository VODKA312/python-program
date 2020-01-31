from random import randint
money = 1000
while money>0:
    print('总资产为:%d' % money)
    first = randint(1,6)+randint(1,6)
    needs_go_on = False
    debt = int(input('说吧，你想下多大的赌注!:'))
    if debt<0 or debt>money:
        print('这样是不行滴,不想跟你玩了')
        debt = int(input('说吧，你想下多大的赌注!:'))
        #这里还是有点问题，如何设置两次以上的赌注问题
    print('第一次总和:%d'% first )
    if first==7 or first == 11:
        print('玩家胜利！')
        money = money+debt
        print('你的剩余资产为%d' % money)
        print('是否想继续？继续请按1，否则请按0,其他选项默认继续')
        if int(input('你的选择是:')) == 1:
            needs_go_on = True
        elif int(input('你的选择是:')) == 0:
            print('祝你走好，下次好运')
            exit()
        else:
            print('error')
        #这里也有一点小问题，并不能实现其他选项默认继续
        #而且你得选择要按两次
    elif first == 2 or first== 3 or first ==12:
        print('你的对手赢了！')
        money = money-debt
        print('你的剩余资产为%d' % money)
        print('是否想继续？继续请按1，否则请按0')
        if int(input('你的选择是:')) == 1:
            #为什么判断正确只需要一次，判定否则的情况需要两次？
            needs_go_on = True
        elif int(input('你的选择是:')) == 0:
            print('祝你走好，下次好运')
            exit()
        else:
            print('error!')
    else:
        needs_go_on = True
        print('不好意思，你得继续')
        while needs_go_on:
            needs_go_on=False
            current = randint(1,6)+randint(1,6)
            if current == 7:
                print('你的对手赢了！')
                money=money-debt
                print('你的剩余资产为%d' % money)
                print('是否想继续？继续请按1，否则请按0,其他选项默认继续')
                if int(input('你的选择是:')) == 1:
                    needs_go_on = True
                elif int(input('你的选择是:')) == 0:
                    print('祝你走好，下次好运')
                    exit()
                else:
                    print('error!')
            elif current == first:
                print('玩家胜利！')
                money=money+debt
                print('你的剩余资产为%d' % money)
                print('是否想继续？继续请按1，否则请按0,其他选项默认继续')
                if int(input('你的选择是:')) == 1:
                    needs_go_on = True
                elif int(input('你的选择是:')) == 0:
                    print('祝你走好，下次好运')
                    exit()
                else:
                    print('error!')
            else:
                needs_go_on = True
print('你破产了')
exit()

