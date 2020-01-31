for num in range(100,999):
    high = num // 100
    mid = (num // 10)%10
    low = num % 10
    if high ** 3 + mid ** 3 + low ** 3 == num:
        print(num)
