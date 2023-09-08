"""
Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with parentheses/round brackets.

"""

# create tuple
student_name = ('Paary','Yusoof','Khairunnadiya','Meiyarasan','CT Wong','Hamizan','Yusry','Yusoof','CT Wong')
print(student_name)

# return data type of tuple variable
print(type(student_name)) # class tuple

# access item from the tuple
print(student_name[3]) # Meiyarasan
print(student_name[6]) # Yusry
print(student_name[-4]) # Hamizan
print(student_name[2:6])
print(student_name[-7:-3])
print(student_name[:2])
print(student_name[2:])
print(student_name[::2])
print(student_name[::4])

# cannot change the item
student_name[1] = 'Farahanim'
#'tuple' object does not support item assignment

# find length of tuple
print(len(student_name))

# create tuple with the one item
employee_id = (100,)
print(type(employee_id)) # <class 'tuple'>
employee_id2 = (100)
print(type(employee_id2)) # <class 'int'>

# tuple with the difference data item
student = (100,'CT Wong',60,60,120,60.0,'Pass','B')
print(student)

# check item is available or not
if 'CT Wong' in student:
    print('Item is available in the student tuple')
else:
    print('Item is not available in the student tuple')

if 70 in student:
    print('Item is available in the student tuple')
else:
    print('Item is not available in the student tuple')

# combine the tuple variable
tuple1 = (10,20,30,40)
tuple2 = (1,2,3,4)
tuple3 = tuple1 + tuple2
print(tuple1,'\n',tuple2,'\n',tuple3)
tuple1 += tuple3
print(tuple1)

# alternatively way to change item
# convert tuple to list after do the changes then again convert list to tuple
print(tuple2)
list1 = list(tuple2) # convert tuple data structure to list structure
print(type(list1))
print(type(tuple2))
list1 [2] = 30
tuple2 = tuple(list1) # convert list to tuple
print(tuple2)

# Delete tuple
del tuple2
print(tuple2)

# access the tuple item using loop
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1

print()
for i in range (len(tuple1)):
    print(tuple1[i])

# times
print(tuple1*2)

# Return the number of time specify value occur in the tuple
print(tuple1.count(10)) # return how many 10 in tuple1

# Return the index position for the specify value occur in the tuple
print(tuple1.index(10))
print(tuple1.index(1))

# Ex:1
# create library tuple which is storing the access number, name of the book, book price, total number of copy, publisher name

#create tuple
book = ('B1','Speed 2022',30.00,20,'Yus Legacy Sdn Bhd')
print(book)

#return data type
print(type(book))

# access item
print(book[1])
print(book[-3])

# find the length of the tuple
print(len(book))

# check item is available or not
if 'Speed 2022' in book:
    print('The book is available in the tuple')
else:
    print('The book is not available in the tuple')

# combine the tuple variable
book2 = ('B2','Fast N Loud',25.0,15,'Rayyan Sdn Bhd')
all_book = book + book2
print(all_book)

# access tuple using loop
i = 0
while i < len(all_book):
    print(all_book[i])
    i += 1

for i in range (len(all_book)):
    print(all_book[i])

# Return the number of time specify value occur in the tuple
print(all_book.count(15))

# Return the index position for the specify value occur in the tuple
print(all_book.index(25.0))

# alternatively way to change item
list = list(book)
list[4] = 'YZ Legacy Sdn Bhd'
book = tuple(list)
print(book)

"""
Dictionary

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered, changeable and does not allow duplicates.
"""

student = {
    'regno': 100,
    'name': 'Muhammad Yusri bin Zakaria',
    'mark1': 90,
    'mark2': 90,
    'total': 180,
    'avg': 90.0,
    'result': 'Pass'
}
print(student)
print(type(student))

# cannot accept duplicate value

student = {
    'regno': 100,
    'name': 'Muhammad Yusri bin Zakaria',
    'mark1': 90,
    'mark2': 90,
    'total': 180,
    'avg': 90.0,
    'result': 'Pass',
    'mark1': 70,
    'result': 'Fail'
}
print(student)

# access information from dictionary
print(student['name'])
print(student['total'])
x = student.get('name')
print(x)

# find length of dictionary
print(len(student))

# display all the keys from dictionary
x = student.keys()
print(x)

# display all the values from dictionary
x = student.values()
print(x)

# checking item available or not
if 'result' in student:
    print('Result is available')
else:
    print('Result is not available')

if 'grade' in student:
    print('Grade is available')
else:
    print('Grade is not available')

# change values of the specific key
student['name'] = 'wong'
print(student)

student.update({'name': 'Yusri'})
print(student)

student.update({'grade': 'A'})
print(student)

# remove item from the dictionary
student.pop('result')
print(student)

# remove the last item from dictionary
student.popitem()
print(student)

# remove all item from dictionary
student.clear()
print(student)

# remove dictionary from memory
del student
print(student)

# copy an item from one dictionary to another dictionary
student2 = student.copy()
print(student2)
print(type(student2))

# using dictionary constructor to copy the items from the one dictionary to another dictionary
student3 = dict(student2)
print(student3)

# nested list
list1 = [10,20,30,[40,50,60],70,80,90]
print(list1)
print(list1[2])
print(list1[5])
print(list1[3])
print(list1[3][1])

name_list = ['Nadia',['Yusoof','Wong'],['Danial','Meiyarasan'],'Yusri',['Hamizan']]
print(len(name_list))
print(name_list[2])
print(name_list.index('Yusri'))
# print(name_list.index('Hamizan')) ValueError: 'Hamizan' is not in list

# nested dictionary
library = {
    'book1': {
        'accno': 100,
        'title': 'Python programming',
        'author': 'Khairunnadhiya',
        'year': 2023,
    },
    'book2': {
        'accno': 101,
        'title': 'SQL Server',
        'author': 'Khairunnadhiya',
        'year': 2023,
    },
    'book3': {
        'accno': 102,
        'title': 'SQL Server',
        'author': 'Khairunnadhiya',
        'year': 2023,
    }
}
print(library)
print(library['book3'])

book1 = {
        'accno': 100,
        'title': 'Python programming',
        'author': 'Khairunnadhiya',
        'year': 2023,
}
book2 = {
        'accno': 101,
        'title': 'SQL Server',
        'author': 'Yusry',
        'year': 2023,
}

book3 = {
        'accno': 102,
        'title': 'ASP.net',
        'author': 'CT Wong',
        'year': 2023,
}

book4 = {
        'accno': 103,
        'title': 'C#',
        'author': 'Meiyarasan',
        'year': 2023,
}

book5 = {
        'accno': 104,
        'title': 'Algorithm',
        'author': 'Yusoof',
        'year': 2023,
}

library2 = {
    'Book1':book1,
    'Book2':book2,
    'Book3':book3,
    'Book4':book4,
    'Book5':book5,
}
print(library2)
print(library2['Book3'])


# create nested dictionary for employee details
# employee id, name, address, phone no, email, job title, salary

# create employee dictionary
employee = {
    'Employee ID' : 'EMP0001',
    'Employee Name' : 'Muhammad Yusri',
    'Employee Address' : 'Jalan Samudra Utara 2, Taman Samudra,',
    'Employee Phone Number' : '010-2349873',
    'Employee Email' : 'yusri@gmail.com',
    'Job title' : 'Programmer',
    'Salary' : '4000.0',
}

# access information from dictionary
print(employee['Employee Name'])
print(employee['Job title'])
x = employee.get('Employee Name')
print(x)

# display all the keys from dictionary
x = employee.keys()
print(x)

# display all the values from dictionary
x = employee.values()
print(x)

# checking item available or not
if 'Job title' in employee:
    print('Job title is available')
else:
    print('Job title is not available')

# change values of the specific key
employee['Employee Name'] = 'Yusry Rayyan'
print(employee)

employee.update({'Employee Name': 'Yusry Zakaria'})
print(employee)

employee.update({'Gender': 'Male'})
print(employee)

# remove item from the dictionary
employee.pop('Gender')
print(employee)

# remove the last item from dictionary
employee.popitem()
print(employee)

# remove all item from dictionary
employee.clear()
print(employee)

# remove dictionary from memory
del employee
print(employee)


