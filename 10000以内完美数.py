L=[]
for n in range(1,10001):
    num=0
    for i in range(1,n):
        if n%i==0:
            num=num+i
    if num==n:
        L.append(n)
print(L)
