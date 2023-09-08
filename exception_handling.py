#Exception Handling
"""
#Exception Handling

**Two types errors**

1.Syntax errors and
2.Logical errors (Exceptions).

Errors are the problems in a program due to which the program will stop the execution.

Exceptions are raised when some internal events occur which changes the normal flow of the program.

The **try** block lets you test a block of code for errors.

The **except** block lets you handle the error.

The **finally** block lets you execute code, regardless of the result of the try- and except blocks.

The **raise** block lets you through own exception

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
"""

# syntax error
# a = 10 +
# print(a) # SyntaxError: invalid syntax

# a = 10 + b
# print(a) # name 'b' is not defined

# if 10 < 5
    # print('10 is less than 5') #SyntaxError: invalid syntax

# exception
print(10 / 5)
print(10 /0) # ZeroDivisionError: division by zero

name = ['Nadia','Wong']
print(name[0])
print(name[3]) # IndexError: list index out of range

# handling exception
try:
    print(x) # try block will generate an exception because x is not defined
    print('Successfully executed')
    print('End of program')
except Exception as ex:
    print(ex) # error will assign to ex
    print('Try to assign any value to x variable')

# Division of two numbers handling exception
try:
    print('Division of two number', 10 / 0)
except Exception as ex:
    print(ex)
    print('Cannot divide by zero')

# to handling specific exception
num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
id = [10,20,30,40,50]
try:
    print('Division of two number', num1 / num2)
    print(id[-7])
except ZeroDivisionError:
    print('Cannot divide by zero')
except NameError:
    print('Try to assign values to variable')
except IndexError:
    print('Cannot fetch the item for the out of index')
else: # not execute if got error
    print('Nothing went wrong')
finally: # to close file
    print('Program successfully end')

# user define exception handling
age = int(input('Enter your age: '))
if age <= 0:
    raise Exception('Give any value age')

# data type error
x = 'PHCDC'
if not type(x) is float:
    raise TypeError('Assign any float value to x variable')

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
id = [10,20,30,40,50]
try:
    print('Division of two number', num1 / num2)
    print(id[-7])
except Exception:
    print('Exception is occurs')
except ZeroDivisionError:
    print('Cannot divide by zero')
except NameError:
    print('Try to assign values to variable')
except IndexError:
    print('Cannot fetch the item for the out of index')
else: # not execute if got error
    print('Nothing went wrong')
finally: # to close file
    print('Program successfully end')

# nested exception
try:
    5 / 0
except ZeroDivisionError as ex:
    try:
        raise Exception('User define exception')
    except Exception as e:
        print('Exception is occur', ex,e)
finally:
    print('Program end')
print(help(Exception))

try:
    fn = input('Enter file name')
    fp = open(fn, 'w')
    for i in range (1,6):
        fp.write(str(i) + '\n')
    fp.close()

    fn = input('Enter file name: ')
    fp = open(fn, 'r')
    for line in fp:
        print(line)
except FileNotFoundError:
    print(fn, 'is not available in the directory')
except Exception as e:
    print(e)
    print('file is not available')
finally:
    fp.close()

fp = open('test.txt','r')

# user defined function
print(help(print))

# create user define function to read name of the student
def readname(): # default parameter
    name = input('Enter the name')
    print(name)

# calling the readname function
readname()
print('End of the program')

# function with return statement
def readname():
    name = input('Enter the name')
    return name
# call the function
print(readname())
print('End of the program')

# addition of two number using function
def addition():
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    return num1 + num2

print('Addition of two numbers', addition())

# function woth argument
def addition(num1, num2):
    return num1 + num2

print('Addition of two numbers =', addition(10,20)) # value pass to variable in function

# substraction of two number using argument
def subtract(num1, num2):
    return num1 - num2

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
print('subtraction of two numbers', subtract(n1, n2))

# default parameter
def subtract(num1, num2 = 10):
    return num1 - num2

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))
print('subtraction of two numbers', subtract(n1, n2))
print('subtraction of two numbers', subtract(n1))

# multiple function
def add():
    print('Addition')
def sub():
    print('Subtraction')
def mul():
    print('Multiply')
def div():
    print('Division')

add()
sub()
mul()
div()

# simple calculator using multiple function : add,sub,mul,div
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def mod(num1, num2):
    return num1 % num2
def floor(num1, num2):
    return num1 // num2

backtomenu = 'y'
while backtomenu == 'y':

    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))

    print ('1--Addition')
    print ('2--Subtraction')
    print ('3--Multiplication')
    print ('4--Division')
    print ('5--Modulus')
    print ('6--Floor Division')

    choice = int(input('Enter your choice'))

    if choice == 1:
        print ('Addition of two numbers: ', add(num1,num2))
    elif choice == 2:
        print('Subtraction of two numbers: ', sub(num1,num2))
    elif choice == 3:
        print('Multiplication of two numbers: ', mul(num1,num2))
    elif choice == 4:
        print('Division of two numbers: ', round(div(num1,num2),2))
    elif choice == 5:
        print('Modulus of two numbers: ', mod(num1,num2))
    elif choice == 6:
        print('Floor of two numbers: ', floor(num1,num2))
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()

    """
    Arbitary argument:
    If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
    This way the function will receive a tuple of arguments, and can access the items accordingly
    """

    def display_names(*n1):
        print(n1)
    display_names('Danial','Yusry','Hamizan','Yusoof','Khairun')

    # arbitary keyword argument

    def display_names(**n1):
        print(n1['name2'])
    display_names(name1='Danial',name2='Yusry',name3='Hamizan',name4='Yusoof',name5='Khairun')

# find factorial given number using function
def find_fact():
    num = int(input('Enter number to find factorial'))
    i = 1
    fact = 1
    while i <= num:
        fact = fact * i
        i += 1
    return fact
print('Factorial of given number = ', find_fact())


# find sum of digit using function
def sumof_digit():
    num = int(input('Enter number to find sum of digit'))
    sum = 0
    while num > 0:
        remainder = num % 10
        sum += remainder
        num //= 10
    return sum
print('The sum of digit = ', sumof_digit())


# display the first 20 fibonacci numbers
def fibonacci():
    num = int(input('Enter number'))
    f = 0
    s = 1
    print(f)
    print(s)
    series = 3
    while series <= num:
        t = f + s
        print(t)
        f = s
        s = t
        series += 1
fibonacci()

# check a given number is prime or not
def check_prime():
    num = int(input('Enter number to check'))
    for i in range(2,int(num)):
        print(i)
        if num % i == 0:
            print(num, 'is not prime')
            break
    else:
        print(num,' is prime number')
check_prime()


# calculate student mark list using function
def calc_mark():
    malay = int(input('Enter malay mark'))
    english = int(input('Enter english mark'))
    science = int(input('Enter science subject'))
    sum = malay + english + science
    return sum
print('Total of student mark= ', calc_mark())


# display/calculate student mark list using function
# id, name, mark1, mark2
# total, avg, grade, result
# then display and calculate

def student_mark():
    studentregno = int(input('Enter student registration number'))
    name = input('Enter your name')
    malay = int(input('Enter mark of malay subject'))
    science = int(input('Enter mark of science subject'))
    maths = int(input('Enter mark of maths subject'))
    total = malay + science + maths
    avg = total / 3

    print('Student Reg No: ', studentregno)
    print('Name: ', name)
    print('Malay subject mark: ', malay)
    print('Science subject mark: ', science)
    print('Maths subject mark: ', maths)
    print('Total marks: ', total)
    print('Total average ', avg)

    if malay >= 50 and science >= 50 and maths >= 50:
        result = 'Pass'
        print('Result: ', result)
        if avg >= 90:
            print('Grade = A+')
        elif avg >= 70:
            print('Grade = A')
        elif avg >= 60:
            print('Grade = B+')
        elif avg >= 50:
            print('Grade = B')
    else:
        result = 'Fail'
        print('Result', result)
        print('Grade: -')
    print('end')
student_mark()





