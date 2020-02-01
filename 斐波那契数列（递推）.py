def firbo_2(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
for i in range(20):
    print(firbo_2(i))
