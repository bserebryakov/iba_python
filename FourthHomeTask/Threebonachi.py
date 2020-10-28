def count_threebonachi(n):
    a = b = 0
    c = 1
    for i in range(n):
        yield c
        sum = a + b + c
        a = b
        b = c
        c = sum


for x in count_threebonachi(35):
    print(x)