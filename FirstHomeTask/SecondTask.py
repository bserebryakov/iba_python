def get_sum(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum

def convert_number_to_ticket_form(number):
    numbers_list = [int(x) for x in str(number)]
    zero_number = 6 - len(numbers_list)
    return str('0' * zero_number) + str(number)

for num in range(999999):
        if get_sum(num) % 7 == 0:
            if get_sum(num + 1) % 7 == 0:
                print("Two neighbour tickets may be lucky, for example: ")
                print("Lucky number: " + convert_number_to_ticket_form(num))
                print("Next lucky number: " + convert_number_to_ticket_form(num + 1))
                break












