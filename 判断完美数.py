num=0
n=int(input('请输入一个数字:'))
for i in range(1,n):
    if n%i==0:
        num=num+i
if num==n:
    print('此数是完美数')
else:
    print('不完美，口球！')

