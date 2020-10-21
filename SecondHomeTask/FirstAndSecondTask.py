def show_rectangle(a, b, symbol):
    mas = []
    for i in range(a):
        mas.append([])
        for j in range(b):
            mas[i].append(symbol)
    for row in mas:
        for elem in row:
            print(elem, end=' ')
        print()

def square_divide():
    return print("______________________")

def cut_rectangle(a, b, squares_number = 0):
    if a == b:
        show_rectangle(a, a, squares_number + 1)
        square_divide()
        return squares_number + 1
    if a < b:
        show_rectangle(a, b - a, squares_number + 1)
        square_divide()
        return cut_rectangle(a, b - a, squares_number + 1)
    show_rectangle(a - b, b, squares_number + 1)
    square_divide()
    return cut_rectangle(a - b, b, squares_number + 1)

print("Input a and b of the rectangle: ")
a = int(input())
b = int(input())
print("Result squares: \n")
print("Square numbers: ", cut_rectangle(a, b))













