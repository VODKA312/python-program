#元素切片
str2='abcd1234'
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
#计算字符串长度
s3='hello,sb'
print('字符串的长度为%d '%len(s3))
#获得首字母大写的拷贝
print('s3首字母大写的拷贝是:%s'% s3.capitalize())
#获得每个单词首字母大写的拷贝
print('s3每个单词首字母大写的拷贝是:%s'% s3.title())
#获得字符串中每个字母大写后的拷贝
print('每个字母大写的拷贝:%s' % s3.upper())
#查找子串的位置，返回最后的位置
print(s3.find('sb'))
#查找不到的情况,返回-1
print(s3.find('shit'))
#如果用index查找查找不到会发现异常
#print(s3.index('shit'))
#将字符串以指定的宽度居中并在两侧填充指定的字符
print(s3.center(50,'*'))
print(s3.rjust(50,' '))
print(s3.ljust(50,' '))
#检查字符串的格式
print(s3.isdigit())
print(s3.isalpha())
print(s3.isalnum())
s4='          sb'
print(s4.strip())
#格式化字符串
a,b='sb','ssbb'
print('第一种格式化方法：%s + %s = %s' % (a,b,a+b))
print('第二种格式化方法:{0}+{1}={2}'.format(a,b,a+b))
print(f'语法糖：{a}+{b}={a+b}')

