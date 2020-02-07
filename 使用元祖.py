t=('yyt',19,True,'浙江温州江南皮革城')
print(t)
#可以通过获取元素的下标获取元素
print(t[0])
print(t[3])
#也可以遍历
for member in t:
    print(member)
#不能通过像列表一样通过元素的位置修改元素，否则会返回type error
#例如t[0]='杨狗蛋'
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('杨二狗', 20, True, '浙江温州倒闭了的江南皮革厂')
print(t)
#元祖是可以转化为列表的
person=list(t)
print(person)
#变为列表后可以修改它的元素
person[0]='杨一天'
person[1]=19
#列表可以转化为元祖
person_tuple=tuple(person)
print(person_tuple)
