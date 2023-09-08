# list, tuple, set, dictionary

# list
# are used to store multiple item in a single variable.
# List are one of the datatype in python
# List are created using [] bracket
# List are changeable one

# create list
numbers = [10, 20, 30, 40, 50]
print(numbers)

# create list to store student name
name = ['Ct Wong', 'Farahanim', 'Hamizan', 'Yusoff', 'Yusry', 'Meiyarasan', 'Danial']
print(name)

# create an empty list
age = []
print(age)
# age[0]=10
# print(age)

# Datatype of list
print(type(age))
print(type(name))
print(type(numbers))

# List item
# are order, changeable and allow duplicate value
# List item are index, the first item has indexed [0]
numbers = [10, 10, 20, 20, 40, 40, 30, 30]
print(numbers)

print(numbers[2])
print(numbers[5])
numbers[0] = 100
print(numbers)

# employee list
employee = [101, 'Yusry', 'Programmer', 3000, 24, 'yusry@gmail.com']
print(employee)

# create numbers list
numbers = [10, 20, 30, 40, 50, 10]
# positive index
print(numbers[0])
print(numbers[2])
# negative index
print(numbers[-4])
print(numbers[-6])

# range of indexes
print(numbers[2:4])
print(numbers[0:5])
print(numbers[:3])
print(numbers[3:])
print(numbers[-5:-2])
# print(numbers[-2:-5])

# check if item is existed
print((10 in numbers))
print((100 in numbers))
print((100 not in numbers))
print((10 not in numbers))

# searching name is available or not in the list
name = ['Ct Wong', 'Farahanim', 'Hamizan', 'Yusoff', 'Yusry', 'Meiyarasan', 'Danial']
key = input('Enter the searching name')
if key in name:
    print('{} is available in the list'.format(key))
else:
    print('{} is not available in the list'.format(key))

# cannot fetch out of range index elements
# print(name[7])
# print(name[-10])
# IndexError: list index out of range

# concatenation more than two lists
print([1, 2] + [3, 4] + [5, 6] + [7, 8])
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
list4 = [7, 8]
list5 = list1 + list2 + list3 + list4
print(list5)
list6 = list5 + name
print(list6)

# repeat the list of times
print(list1 * 3)
print(list6 * 10)

"""
List Methods
---------------------------------------------------------------
Method	                Description
---------------------------------------------------------------
append() -Adds an element at the end of the list

clear() -Removes all the elements from the list

copy()	-Returns a copy of the list

count()	-Returns the number of elements with the specified value

extend()	-Add the elements of a list (or any iterable), to the end of the current list

index()	-Returns the index of the first element with the specified value

insert()	-Adds an element at the specified position

pop()	-Removes the element at the specified position

remove()	-Removes the item with the specified value

reverse()	-Reverses the order of the list

sort()	-Sorts the list

"""

numbers = [10, 20, 30, 40, 50, 10, 20, 35]
# to remove item for the list
print(numbers)
numbers.remove(35)
print(numbers)
numbers.remove(10)
print(numbers)
numbers.remove(60)
print(numbers)

# remove the element for the specifies position
numbers.pop(2)
print(numbers)

# remove all the elements
numbers.clear()
print(numbers)

# remove list from the memory
del numbers
print(numbers)

numbers = [10, 20, 30, 40, 50, 10, 20, 35]
print(numbers)
# add element to the existing list
numbers.append(60)
print(numbers)
numbers.append(70)
print(numbers)

tuple1 = 80, 90, 100
print(tuple1)
print(type(tuple1))
numbers.append(tuple1)
print(numbers)
print(numbers[9])
print(numbers[10])
print(numbers[10][1])

# insert value at index position
numbers.insert(1, 15)
print(numbers)
numbers.insert(10, 95)
print(numbers)

numbers = [10, 20, 30, 40, 50, 10, 20, 35]
print(numbers)
# arrange list item in ascending order
numbers.sort()
print(numbers)
# arrange list item in descending order
numbers.sort(reverse=True)
print(numbers)

name = ['Ct Wong', 'Farahanim', 'Hamizan', 'Yusoff', 'Yusry', 'Meiyarasan', 'Danial']
print(name)
# sort name in alphabetical order
name.sort()
print(name)
name.sort(reverse=True)
print(name)

# display index position
print(name.index('Farahanim'))
# print(name.rindex('Farahanim'))
name.reverse()
print(name)

# exercise 1
"""
1-Add new employee name to the list
2-Search employee name from the list
3-Remove employee name from the list
4-Display all the employee name
"""

# set
# definition of set are used to store multiple items in single variable
# collection both unordered and un-index
# sets are return with a { }

# create student set
student = {'ct wong', 'farahanim', 'hamizan', 'yusry'}
print(student)
print(type(student))

# len of set(counter for number in set)
print(len(student))

# store multiple data items
employeeset = {101, 'Danial', 1500.0}
print(employeeset)

# create a set with use set constructor
employeeset = set((101, 'Danial', 1500.0))
print(employeeset)

# access items
for x in employeeset:
    print(x)

# check items
print('Danial' in employeeset)
print('hamizan' in employeeset)
print('Danial' not in employeeset)

# add item
employeeset.add('data analyst')
print(employeeset)

# create student set
student = {'KL', 'danial@gmail.com', 'SEL', 'hamizan@gmail.com'}
# add student set to employee set
employeeset.update(student)
print(employeeset)

# remove item from set
employeeset.discard('KL')
print(employeeset)
employeeset.discard('JB')
print(employeeset)
# or
employeeset.remove('hamizan@gmail.com')
print(employeeset)
employeeset.remove('SEL')
print(employeeset)

# Remove item using pop function - random item will be removed
x = employeeset.pop()
print(x)
print(employeeset)

# remove all items from set
employeeset.clear()
print(employeeset)

# remove set from memory
del employeeset
print(employeeset)

# join two set
set1 = {10, 20, 30, 40}
set2 = {50, 60, 70, 20, 30}
print(set1)
print(set2)
set3 = set1.union(set2)  # union returns a new set with all items from both set
# exclude any duplicate item
print(set3)

# intersect function
set4 = set1.intersection(set2) # returns a new set with common items
print(set4)

# symmetric
set1.symmetric_difference(set2)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)
