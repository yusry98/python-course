# exercise 1
num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

if num1 > num2:
    print(num1, 'is the largest number')
elif num2 > num1:
    print (num2, 'is the largest number')
else:
    print(num1,' is equal to ',num2)

exit()

# exercise 2
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
while i <= 5: # outer loop
    j = 0
    while j < i: # inner loop
        print (letters[j], end=' ')
        j += 1
    print ()
    i+=1

# exercise 3
num = int(input('Enter the value: '))
for y in range (1,17):
    print(y, 'X', num, '=', y * num)