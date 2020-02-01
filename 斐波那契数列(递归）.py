def firbo_1(n):
    if n==0 or n==1:
        return n
    else:
        return firbo_1(n-1)+firbo_1(n-2)
for i in range(0,20):
    print(firbo_1(i),end=' ')
    
