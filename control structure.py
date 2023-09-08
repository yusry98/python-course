# simple if statement
# check whether the age of the person is greater than or equal to 18
age = int(input('Enter your age'))
if age >= 18:
    print('Your age is greater than or equal to 18')
print('program end')

# check whether the number is greater than 10
num = int(input('Enter your number'))
if num > 10:
    print('Your number is greater than 10')
print('program end')

# multiple if statement
code = int(input('Enter your code'))
if code == 1:
    print('Your code is one')
if code == 2:
    print('Your code is two')
if code == 3:
    print('Your code is three')

# Nested if statement
code = int(input('Enter your code'))
color = input('Enter your favourite color')
if code == 1:
    if color == 'red':
        print('Your code is one and favourite color is red')
print('exit')

# Check whether the person is eligible to vote in Malaysia
age = int(input('Enter your age'))
country = input('Enter your country name')
if age >= 18:
    if country == 'Malaysia':
        print('You eligible to vote in Malaysia country')
print('exit')

# if else statement
code = int(input('Enter your code'))
if code == 1:
    print('Your code is one')
else:
    print('Your code is not equal to one')
print('end')

# check whether favourite color is red or not
color = input('Enter your favourite color')
if color == 'red' or color == 'Red' or color == 'RED' :
    print('Your favourite color is ', color)
else:
    print('Your favourite color is not ', color)
print('end')


age = int(input('Enter your age'))
country = input('Enter your country name')
if age >= 18:
    if country == 'Malaysia':
        print('You eligible for vote in Malaysia country ')
        print('verification success')
    else:
        print('You are not eligible for vote in Malaysia country')
        print('Unsuccessful verification')
else:
        print('You not eligible for vote', age)
        print('unsuccessful verification')
print('end')

# if-elif-else
marks = int(input('Enter your mark'))
if marks >= 90:
    print('Grade D')
elif marks >= 60:
    print('Grade is A')
elif marks >= 50:
    print('Grade is B')
else:
    print('Grade is C')

# traffic light checking
colors = input('Enter light color')
if colors == 'red' or colors == 'Red' or colors == 'RED':
    print('Stop Driving')
elif colors == 'green' or colors == 'Green' or colors == 'GREEN':
    print('Start driving')
elif colors == 'orange' or colors == 'Orange' or colors == 'ORANGE':
    print('Prepare to stop')
else:
    print('Invalid color selection try again')

"""
1. Write a python program to check whether the given number is odd or even
2. Write a python program to check whether the given number is positive, negative or zero
"""

# exercise 1
num = int(input('Enter your number'))
result = num % 2
if result == 0:
    print('The given number is even number which is', num)
else:
    print('The given number is odd number which is', num)

# exercise 2
num = int(input('Enter your number'))
if num > 0:
    print('The given number is positive')
elif num < 0:
    print('The given number is negative')
else:
    print('The given number is zero')

"""
3. Write a python program to display student details. To get studentregno, name,malay, science, maths mark information from the user and calculate total, average, result 
   and find the grade of the student with following condition    
    avg>=90   'A+'
    avg>=70   'A'
    avg>=60   'B+'
    avg>=50   'B'
    avg<50     '-'
"""

# exercise 3

studentregno = int(input('Enter student registration number'))
name = input('Enter your name')
malay = int(input('Enter mark of malay subject'))
science = int(input('Enter mark of science subject'))
maths = int(input('Enter mark of maths subject'))
total = malay + science + maths
avg = total / 3

print('Student Reg No: ', studentregno)
print('Name: ',name)
print('Malay subject mark: ', malay)
print('Science subject mark: ', science)
print('Maths subject mark: ', maths)
print('Total marks: ', total)
print('Total average ', avg)

if malay >=50 and science >= 50 and maths >= 50:
    result='Pass'
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
