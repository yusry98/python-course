#D15P1: F2C CONVERSION
f = float(input('Enter Fahrenheit temperature'))
c = round(5/9 * (f-32),2)
print('Fahreinheit temperature {} is the same as {} degrees Celsius'.format(f,c))


#D15P2: FINAL VELOCITY
u = float(input('Enter inital velocity'))
a = float(input('Enter acceleration'))
t = int(input('Enter time duration'))
if t >= 0:
    v = round(u + a * t, 2)
    print('The final velocity is {}'.format(v))
else:
    print('Time can take non negative real values only.Try again')


#D15P3: DISPLACEMENT COVERED
u = float(input('Enter inital velocity'))
a = float(input('Enter acceleration'))
t = int(input('Enter time duration'))
if t >= 0:
    d = round((u * t) + (1 / 2 * a * t**2), 2)
    print('The displacement is {}'.format(d))
else:
    print('Time can take non negative real values only.Try again')


#D15P4: NUMBER OF DAYS
s = int(input('Enter number of seconds: '))
hh = s // 3600
mm = s % 3600 // 60
ss = s % 60

print('{}:{}:{}'.format(hh,mm,ss))


#D15P5: LEAP YEAR
year = int(input("Enter year"))
if year % 4 == 0:
    print('True')
else:
    print('False')


#D15P6: REVERSE THE NUMBER
number = int(input('Enter number to find reverse of the number'))
# using string slicing
print(str(number)[::-1])


#D15P7: DISPLAY MULTIPLICATION TABLE
mul = int(input('Enter multiplier'))
range = int(input('Enter range'))
num = 1

while num <= range:
    p = str(num * mul)
    print(num, 'X', mul, ' = ', p)
    num = num + 1


#D15P8: PRIME NUMBER CHECKING
check_num = int(input('Enter number to check'))
for i in range(2,int(check_num)):
    if check_num % i == 0:
        print(check_num, 'is not prime')
        break
else:
    print(check_num,' is prime number')

