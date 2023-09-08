"""
To create python program for simple calculator-getting choices from user like

output
Enter first number 5
Enter second number 10

1--> Addition
2--> Subtraction
3--> Multiplication
4--> Division
5--> Floor Division
Enter your  choice
1
Addition of two numbers=15

Do you want to continue press y otherwise press n: y

1--> Addition
2--> Subtraction
3--> Multiplication
4--> Division
5--> Floor Division
Enter your  choice
3
Addition of two numbers=50

Do you want to continue press y otherwise press n: n

"""
backtomenu = 'y'
while backtomenu == 'y':

    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))

    print('1 --> Addition')
    print('2--> Subtraction')
    print('3--> Multiplication')
    print('4--> Division')
    print('5--> Floor Division')

    choice = int(input('Enter your choice'))

    if choice == 1:
        print ('Addition of two numbers: ', num1 + num2)
    elif choice == 2:
        print ('Subtraction of two numbers: ', num1 - num2)
    elif choice == 3:
        print ('Multiplication of two numbers: ', num1 * num2)
    elif choice == 4:
        print('Division of two numbers: ', num1 / num2)
    elif choice == 5:
        print('Floor division of two numbers: ', num1 // num2)
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()






