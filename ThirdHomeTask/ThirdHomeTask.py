from datetime import datetime, date

class Student:
    __surname = " "
    __name = " "
    __lastname = " "
    __birthday = date.today()
    __address = " "
    __phonenumber = " "
    __faculty = " "
    __course = 0
    __group = 0

    def __init__(self, surname, name, lastname, birthday, address, phonenumber, faculty, course, group):
        self.__surname = surname
        self.__name = name
        self.__lastname = lastname
        self.__birthday = birthday
        self.__address = address
        self.__phonenumber = phonenumber
        self.__faculty = faculty
        self.__course = course
        self.__group = group

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_lastname(self):
        return self.__lastname

    def get_age(self):
        return self.__birthday

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber

    def get_faculty(self):
        return self.__faculty

    def get_course(self):
        return self.__course

    def get_group(self):
        return self.__group

    def __str__(self):
        today = date.today()
        date_of_birth = datetime.strptime(self.__birthday, "%d %m %Y")
        age = "Age: %s year(s)" % (today.year - date_of_birth.year -
                                 ((today.month, today.day) < (date_of_birth.month, date_of_birth.day)))
        return str(self.__surname) + " " + str(self.__name) + " " + str(self.__lastname) + ", " + age\
               + ", " + str(self.__address) + " " + str(self.__phonenumber) + ", " + str(self.__faculty) \
               + ", " + str(self.__course) + ", " + str(self.__group)

students_list = [
    Student("Bogdan", "Serebryakov", "Evgenyevich", "05 01 1999", "pr. Mira", "+375291235432", "FITR", 5, 107),
    Student("Elizaveta", "Taras", "Alexandrovna", "01 12 2000", "Pushkina st.", "+375293456775", "FITR", 5, 107),
    Student("Mariya", "Pominova", "Sergeevna", "14 04 1998", "Alibegova st.", "+375296576321", "MTF", 4, 101),
    Student("Andrey", "Pominov", "Sergeevich", "17 08 1999", "Alibegova st.", "+375291323456", "FITR", 5, 107),
    Student("Denis", "Nemcov", "Georgevich", "13 05 2000", "Yakub Kolasa st., d.32", "+375446457865", "FITR", 5, 107),
    Student("Sasha", "Yaroshko", "Sergeevna", "14 04 1998", "Alibegova st.", "+375293900339", "MTF", 4, 101),
    Student("Peter", "Naryshkin", "Dmitrievich", "17 08 1999", "Alibegova st.", "+375298876324", "FITR", 5, 107),
    Student("Genadiy", "Kadyrov", "Petrovich", "13 05 2000", "Yakub Kolasa st., d.31", "+375448876324", "FITR", 5, 102),
    Student("Vladislav", "Putin", "Sergeevna", "14 04 1998", "Alibegova st., d.17", "+375298842819", "EF", 4, 101),
    Student("Egor", "Tramp", "Sergeevich", "17 08 1999", "Alibegova st.", "+375298204610", "FTUG", 3, 107),
    Student("Dmitry", "Sviridov", "Evgenyevich", "13 05 2000", "Yakub Kolasa st., d.32", "+375442164530", "FITR", 2, 107),
]

def get_students_by_group_number(group):
    print("List of the students by group: \n")
    for i in students_list:
        if i.get_group() == group:
            print(i.__str__())

def get_students_by_faculty(faculty):
    print("List of the students by faculty name: \n")
    for i in students_list:
        if i.get_faculty() == faculty:
            print(i.__str__())

print("Put the faculty name: ")
get_students_by_faculty(input())
print()
print("Put the group number: ")
get_students_by_group_number(int(input()))
