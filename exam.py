
list2 = ["List" , "Dictionary", "D", "T", "Tuple"]

min(list2)

list2[1][0]

list2[-2]

list2[1][-1]


class test:
    def __init__(self, a="Hello"):
        self.a = a

    def show(self):
        print(self.a)


t = test("World")

def __init__(self, s):

    self.s = s

def __add__(self, str2):

    return len(self.s) + len(str2.s)

s1, s2 = MyStr("hey"), MyStr("hello")

print(s1 + s2)

class Test():
def __init__(self, num):
           self.num = num
t1 = Test(2)
t2 = Test(3)
t2 = t1
t1.num = 4
print(t2.num)


class MyString(object):

    def __init__(self, s):
        self.s = s

    def __eq__(self, s):
        if self.s[0] == s.s[0]:
            return True

        return False


s1 = MyString("Heyyy")

s2 = MyString("Hello")

if s1 == s2:

    print("yes")

else:

    print("No")

A = {50,40}

B = {10,20,40,50}

print(A < B)

import numpy

a = [[1, 2], [3, 4]]

b = [[1, 2], [3, 4]]

print(a + b)


class MyStr:

    def __init__(self, s):
        self.s = s

    def __add__(self, str2):
        return len(self.s) + len(str2.s)


s1, s2 = MyStr("hey"), MyStr("hello")

print(s1 + s2)

a= 55
b = 32
print(a/b)
print(a//b)
print(a%b)

weekdays = ['sun','mon','tue','wed','thu','fri','sat']

print(type(weekdays))
listAsTuple = tuple(weekdays)
print(listAsTuple)
print(type(listAsTuple))

import numpy

numpy.array([ ])

import array
a = [1, 2, 3]
print (a[-3])
print a[-2]
print a[-1]


names = ['Perak', 'Human', 'Capital', 'Centre']
print(names[-1][-1])

list1 = [1,3,2]
print (list1 * 2)

tuple1 = ("PHCDC")
tupletolist = list(tuple1)
print (tupletolist)

n=int(input("Enter the number to print the tables for:"))
for i in range(1,6):
    print(n,"x",i,"=",n*i)

s1 = input("Enter first string:")
s2 = input("Enter second string:")
a = list(set(s1) & set(s2))
print("The ____?____ are:")
for i in a:
    print(i)

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
print(weekdays.count('mon'))