a = []
counter = 0
print("Input length of the list:")
for i in range(int(input())):
    print("Insert number:")
    a.append(int(input()))
    if a[i] < 0:
        counter += 1

print("Result list: " + str(a))
print("Number of the negatives: " + str(counter))











