std_mark = {70,85,63,42,55}
backtomenu = 'y'
while backtomenu == 'y':

    print('1--> Add mark to the student set')
    print('2--> Search mark from the student mark set')
    print('3--> Remove mark fom the student mark set')
    print('4--> Display all the student mark')

    choice = int(input('Enter your choice'))

    if choice == 1:
        mark = int(input('Enter mark'))
        std_mark.add(mark)
        print('Succesfully added')
    elif choice == 2:
        mark = int(input('Enter mark'))
        print(mark in std_mark)
    elif choice == 3:
        mark = int(input('Enter mark'))
        if mark in std_mark:
            std_mark.remove(mark)
            print(mark, 'is succesfully removed from the list')
        else:
            print(mark, 'is not in the list')
    elif choice == 4:
        print(std_mark)
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()