# -*- coding: utf-8 -*-
#判断你是不是00后的程序
s = input('你的生日年份是:')
birth = int(s)
if s > 2000:
    print('你是可爱的蛋蛋后~o(*￣▽￣*)o');
else:
    print('你是成熟帅气的蛋蛋前');
#注意如果使用强制转换input返回值类型也可以，但是最好不同变量用不同的数据类型
#input的默认返回是string
