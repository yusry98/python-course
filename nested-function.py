# Nested function
def fun1():
    print('Hi! everybody')
def fun2():
    fun1() # Nested function - Function call another function
    print('Welcome to Bigdata class')

# Call the fun2()
fun2()

# Global variable
glob = 10

def f1(): # create f1() function
    global x # Make a local variable as a global access
    x = 20 # local variable
    glob = 30 # local variable
    print('Local variable value =', x)
    print('Global variable inside f1():', glob) # able to access global variable in f1()

def f2(): # create f1() function
    print('Local variable value =', x) #20
    print('Global variable inside f2():', glob) # able to access global variable in f2()

def f3(): # create f1() function
    print('Local variable value =', x)  # 20
    print('Global variable inside f3():', glob) # able to access global variable in f3()

print('Global variable outside all function:' ,glob) # able to access global variable outside all function
f1() # call the f1() function
f2() # call the f2() function
f3() # call the f3() function
print('Local variable value =', x) #20

# Addition of two numbers

# Create function to read to numbers
def read_num():
    global n1,n2 # make a local variable as a global access
    n1 = int(input('Enter the first number'))
    n2 = int(input('Enter the second number'))

# Create function to calculate addition of two numbers
def calculate_add():
    global add
    add = n1 + n2

# Create function to display addition result
def display():
    read_num()
    calculate_add()
    print('Addition of {} + {} = {} '.format(n1,n2,add))

display() # to call display function

"""
studentregno = int(input('Enter the studentregno'))
name = input('Enter your name')
malay = int(input('Enter your malay mark'))
science = int(input('Enter your science mark'))
maths = int(input('Enter your maths mark'))
total = malay + science + maths
avg = total/3
print('studentregno: ', studentregno)
print('name: ', name)
print('malay: ', malay)
print('science ', science)
print('maths ', maths)
print('total ', total)
print('avg ', avg)
if malay >= 50 and science >= 50 and maths >= 50:
    result = 'Pass'
    print('Result:', result)

    if avg >= 90:
        print('Grade A+')
    elif avg >= 70:
        print('Grade A')
    elif avg >= 60:
        print('Grade B+')
    elif avg >= 50:
        print('Grade B')
else:
    result = 'Fail'
    print('Result:', result)
    print('Grade -')
"""

def read_stdmark():
    global regno,std_name,malay,science,math
    regno = int(input('Enter student ID'))
    std_name = input('Enter student name')
    malay = int(input('Enter malay mark'))
    science = int(input('Enter science mark'))
    math = int(input('Enter math mark'))

def calculate_mark():
    global total,avg
    total = malay + science + math
    avg = round(total / 3,2)

def display_result():
    read_stdmark()
    calculate_mark()
    print('Student ID: ', regno)
    print('Student name', std_name)
    print('Malay mark', malay)
    print('Science mark', science)
    print('Math mark', math)
    print('Total mark: {} + {} + {} = {} '.format(malay, science, math, total))
    print('Average mark: ({} + {} + {}) / 3 = {} '.format(malay, science, math, avg))
    if malay >= 50 and science >= 50 and math >= 50:
        result = 'Pass'
        print('Result:', result)
        if avg >= 90:
            print('Grade A+')
        elif avg >= 70:
            print('Grade A')
        elif avg >= 60:
            print('Grade B+')
        elif avg >= 50:
            print('Grade B')
    else:
        result = 'Fail'
        print('Result:', result)
        print('Grade -')

display_result()

# sum of n numbers using function
num = int(input('Enter the number '))
s = 0
for i in range (1,num + 1):
    s += i
print('Sum of {0} numbers = {1}'.format(num,s))

#or
def find(num):
    s = 0
    for i in range(1,num + 1):
        s += i
    return s

num = int(input('Enter the number'))
print('Sum of {0} numbers = {1}'.format(num,find(num)))

#or using recursive
def find(num):
    if num == 0:
        return 0
    else:
        return num + find(num-1) # recursive function - function call itself

num = int(input('Enter the number'))
print('Sum of {0} numbers = {1}'.format(num,find(num)))

# find factorial number using recursive
def find_fact(num):
    if num == 0:
        return 1
    else:
        return num * find_fact(num-1)

num = int(input('Enter number to find factorial'))
print('Factorial of {0} numbers = {1}'.format(num,find_fact(num)))

# To generate Fibonacci series using recursive function
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))
num = int(input('Enter number'))
for i in range(num):
    print(fibonacci(i))


