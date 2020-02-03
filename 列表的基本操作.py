list1=[1,2,3,4,5,6,10]
print(list1)
list2=list1*3
print(list2)
list3=['car','audi','hahaha']
print(list3[1].upper())
print(list1[1])
#修改元素
list1[1]=200
print(list1)
#用下标遍历
for index in range(len(list1)):
    print(list1[index],end=' ')
print('\n')
for index in range(0,len(list1)):
    print(list1[index],end=' ')
print('\n')
#用for循环遍历元素
for elem in list1:
    print(elem)
for index,elem in enumerate(list1):
    print(index,elem)
list1.append(100)
#用append方法添加元素，默认在最末尾
list1.insert(1, 400)
#用insert方法添加元素，直接取代掉那个位置的元素
print(list1)
list1 += [1000,2000,3000]
#列表相加，相加的列表也默认添加到最末尾
print(list1)
if 3 in list1:
    list1.remove(3)
#remove方法是通过元素删除，pop是通过下标
list1.pop(0)
#清空列表
list1.clear()
print(list1)
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
fruits2=fruits[1:4]
print(fruits2)
#完整切片
fruits3 = fruits[:]
#开始的位置是-3,切到-1为止
fruits4 = fruits[-3:-1]
print(fruits4)
#反向切片
fruits5=fruits[::-1]
print(fruits5)
