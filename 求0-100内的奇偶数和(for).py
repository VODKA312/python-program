# -*- coding: utf-8 -*-
#for循环方法
sum1 = 0
for x in list(range(0,101)):
    if x%2 != 0:
        sum1 = sum1+x
print('奇数和是%d' % sum1)
sum2 = 0
for x in list(range(0,101)):
    if x%2 ==0:
        sum2=sum2+x
print('偶数和是%d' % sum2)