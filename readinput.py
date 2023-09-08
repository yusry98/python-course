# Read input from user and display the personal information

name=input('Enter your name')
age=input('Enter your age')
print('Your name is ' + name + '\nYour age is '+age)
# OR
print('Your name is', name)
print('Your age is', age)

# To create python program to find addition of two numbers

num1=input('Enter first number')
num2=input('Enter second number')
sum = int(num1) + int(num2)
print("The sum is: ", sum)
# OR
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
sum = num1 + num2
print("The sum is: ", sum)

# variable and datatype

intnumber=10
floatnumber=10.5
stringname='PHCDC'

print(type(10))
print(type(name))
print(type(True))
print(type(10j))

#Arithmetic operator
"""
+ addition
- substraction
* multiplication --return float value
/ Division
% Modulus
//Floor --return int value
"""

print('Addition value = ', 10 + 20)
print('Subtraction value = ', 20 - 10)
print('Multiplication value = ', 2 * 4)
print('Division value = ', 4 / 2)
print('Floor value = ', 4 // 2)
print('Modulus value =', 4 % 3)

# Create python program for simple calculator - Getting input from user

# Addition
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
sum= num1 + num2
print('The sum is = ', sum)

# Subtraction
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result= num1 - num2
print('The subtraction is = ', result)

# Multiplication
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result= num1 * num2
print('The multiplication is = ', result)

# Division
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result= num1 / num2
print('The division is = ', result)

# Modulus
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result= num1 % num2
print('The modulus is = ', result)

# Floor
num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
result= num1 // num2
print('The floor is = ', result)

# Find area of circle with using the formula PI*R*R

r = float(input('Enter your radius'))
result = 3.142 * r * r
print('Area of circle is = ', result)

# Find area of rectangle with using the formula length*breadth

length = float(input('Enter length'))
breadth = float(input('Enter breadth'))
result = length * breadth
print('Area of rectangle = ', result)

# Find area of triangle with using the formula 1/2bh

b = float(input('Enter base'))
h = float(input('Enter height'))
result = 1/2 * b * h
print('Area of triangle = ', result)

# Using import math

import math
r = float(input('Enter your radius'))
print('Area of circle = ', math.pi*r**r)

# Relational operator
"""
<
>
<=
>=
==
!=
"""

print('10<5',10<5) # False
print('5<10',5<10) # True
print('5<5',5<5) # False
print('5<=5',5<=5) # True
print('10>5',10>5) # True
print('10>=5',10>=5) # True
print('5>10',5>10) # False
print('10==10',10==10) # True
print('10!=11',10!=11) # True

# Check code is valid or not
code=int(input('Enter your code'))
if code==1:
    print('You entered valid code')
else:
    print('You entered invalid code')

print('program end')


# To check whether the person is eligible for vote

age=int(input('Enter your age'))
if age>=18:
    print('Congratulation')
    print('You are eligible to vote')
else:
    print('Sorry')
    print('You are not eligible to vote')

print('program end')

# Logical Operators

print('10>5 and 5<10', 10>5 and 5<10)

# Check code and color is valid or not

code=int(input('Enter your code'))
color=input('Enter your color')
if code==1 and color=='Red':
    print('You entered valid code and color')
    print('Successfully verified')
else:
    print('You entered invalid code and color')
    print('Verification unsuccess')
print('program end')

# Other example

age=int(input('Enter your age'))
country=input('Enter your country')
if age>=18 and country=='Malaysia':
    print('Good')
    print('You are eligible to work')
else:
    print('Sorry')
    print('You are not eligible to work')

print('program end')

#

a=10
print(a)
b=1
print(b)
b+=10
print(b)
b=b-1
print(b)
b+=1
print(b)

b+=1
b-=1
b*=2

#
eval= 100 * 2 % 4 + (10-2) /5
print(eval)

print(35-20/5)

# Identity operator

a=10.90
if type(a) is int:
    print('a is a integer variable')
else:
    print('a is not a integer variable')

a=10
if type(a) is not int:
    print('a is not a integer variable')
else:
    print('a is integer variable')
