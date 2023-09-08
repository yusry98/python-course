
"""
D15P1. F2C Conversion
Write a program that takes as input Fahrenheit temperature.
It converts the input temperature to Celsius and prints out the converted temperature as shown in the example.
The formula for conversion between the two is: C=5/9(F−32),
Where C is the temperature in Celsius and F is the temperature in Fahrenheit.

NOTE:
1.	DO NOT use any prompts in the input().
2.	Use the round() function to round your answer to up to two decimal places. That is, use round(VALUE, 2).
INPUT:
212

OUTPUT:
Fahrenheit temperature 212.0 is the same as 100.0 degrees Celsius.


2. Write a program to check if the given year is a leap year or not.
The program should read an integer (year) from a user. Display the Boolean value:
True if the year is a leap year, False if not.

Input: 2024

Output: True


3.Write a program that takes as input an Integer s,
the number of seconds elapsed for a certain event.
The program converts s to hours (hh), minutes (mm), and seconds (ss)
and prints the output as hh:mm:ss. Note that the input will only be
positive integer values since time cannot be negative.

INPUT: 5

OUTPUT: 0:0:5

INPUT: 3692

OUTPUT: 1:1:32

"""
# question 1
f_temp= input('Enter Fahrenheit temperature')
f_temp_str = float(f_temp)
c_temp = round(5 / 9 * (f_temp_str - 32), 2)
c_temp_str = str(c_temp)
print('Fahrenheit temperature ' + f_temp + ' is the same as ' + c_temp_str)

# question 2
year = int(input("Enter year"))
if year % 4 == 0:
    print('True')
else:
    print('False')

# question 3
import math
s_input = int(input('Enter number of seconds'))
h = int(s_input / 3600)
m = int((s_input-(h * 3600)) / 60)
s = int((s_input - (h * 3600)) - (m * 60))
print(str(h) + ':' + str(m) + ':' + str(s))
#OR
s = int(input('Enter number of seconds: '))
hh = s // 3600
mm = s % 3600 // 60
ss = s % 60

print('{}:{}:{}'.format(hh,mm,ss))
