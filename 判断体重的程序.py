#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
#帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：
# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi=weight/(height*height)
if bmi<18.5:
    print('体重过轻')
elif 18.5<bmi<25:
    print('体重正常')
elif 25<bmi<28:
    print('过重')
elif 28<bmi<32:
    print('肥胖')
else:
    print('严重肥胖！！！')
#这里出现了个小错误需要提醒！
#pyhon是一门动态语言，不需要标名变量类型
#但是需要标名变量在另一个关联变量之前
