# D16P1
# sum of n numbers using function
num = int(input('Enter the number '))
s = 0
for i in range (1,num + 1):
    s += i
print('Sum of natural number {0} is {1}'.format(num,s))

# D16P2
num = int(input("Enter any number: "))
ori_num = num
reverse = 0

while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if ori_num == reverse:
    print('The given {} is palindrome number'.format(ori_num))
else:
    print('The given {} is not palindrome number'.format(ori_num))

# D16P3
num = int(input('Enter the number'))
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
while i <= num: # outer loop
    j = 0

    while j < i: # inner loop
        if i < 2:
            print('_', letters[j],'_', end=' ')
            j += 1
        else:
            print ('_',letters[j], end=' ')
            j += 1
    print ()
    i+=1

# D16P4
num = int(input('Enter the number: '))
i = 0
while i <= num: # outer loop
    j = 0
    while j < i: # inner loop
        print ('*', end=' ')
        j += 1
    print ()
    i+=1

# D16P5
name = input('Enter name to reverse')
print(name[::-1])

# D16P6
country = input('Enter the country ')
distance = int(input('Enter the Distance in Kilometers '))

if country == 'Malaysia':
    if distance >= 1 and distance <=50:
        print('Your shipping fees is : RM 2.5')
    elif distance >= 51 and distance <=100:
        print('Your shipping fees is : RM 4.5')
    elif distance >= 101 and distance <=300:
        print('Your shipping fees is : RM 6.5')
    elif distance >= 301 and distance <=700:
        print('Your shipping fees is : RM 8.0')
    elif distance >= 701:
        print('Your shipping fees is : RM 12.0')

elif country == 'Australia':
    if distance >= 1 and distance <=50:
        print('Your shipping fees is : $ 1.5')
    elif distance >= 51 and distance <=100:
        print('Your shipping fees is : $ 2.5')
    elif distance >= 101 and distance <=300:
        print('Your shipping fees is : $ 3.5')
    elif distance >= 301 and distance <=700:
        print('Your shipping fees is : $ 4.5')
    elif distance >= 701:
        print('Your shipping fees is : $ 7.0')

elif country == 'India':
    if distance >= 1 and distance <=50:
        print('Your shipping fees is : RS 10.0')
    elif distance >= 51 and distance <=100:
        print('Your shipping fees is : RS 15.0')
    elif distance >= 101 and distance <=300:
        print('Your shipping fees is : RS 30.0')
    elif distance >= 301 and distance <=700:
        print('Your shipping fees is : RS 50.0')
    elif distance >= 701:
        print('Your shipping fees is : RS 100.0')

else:
    print('Shipping fee not applicable for this country')
