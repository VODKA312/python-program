for rooster in range(0,20):
    for hen in range(0,33):
        chick = 100-rooster-hen
        if chick/3 + rooster * 5 + hen *3==100:
             print('公鸡有:%d只，母鸡有%d只，小鸡有%d只.' % (rooster,hen,chick))
