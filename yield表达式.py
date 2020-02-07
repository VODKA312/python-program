def square():
    for x in range(4):
        yield x**2
square_gen = square()
for x in square_gen:
    print(x)
