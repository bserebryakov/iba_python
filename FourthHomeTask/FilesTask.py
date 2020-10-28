import os

FIRST_FILE_NAME = "F1.txt"
SECOND_FILE_NAME = "F2.txt"

def read_first_file():
    with open(FIRST_FILE_NAME, 'r') as file:
        text = file.read()
    return text.split('\n')

def write_second_file(words):
    with open(SECOND_FILE_NAME, 'w') as second_file:
        for i in range(1, len(words), 2):
            second_file.write(words[i] + '\n')

def print_file_sizes():
    with open(FIRST_FILE_NAME) as file:
        file.seek(0, os.SEEK_END)
        print("FILE SIZES:\n")
        print("F1.txt: %s" % file.tell())
    with open(SECOND_FILE_NAME) as second_file:
        second_file.seek(0, os.SEEK_END)
        print("F2.txt: %s" % second_file.tell())

write_second_file(read_first_file())
print_file_sizes()


