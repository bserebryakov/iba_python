from random import randint

print("Input length of the list:")
numbers = [randint(0, 99) for i in range(int(input()))]
print("Result list: " + str(numbers))
print("Input index of the removing element:")
numbers.pop(int(input()))
print("Result list after removed element: " + str(numbers))










