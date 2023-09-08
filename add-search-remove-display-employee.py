#exercise 1
"""
1-Add new employee name to the list
2-Search employee name from the list
3-Remove employee name from the list
4-Display all the employee name
"""

name_list = ['Ct Wong','Farahanim','Hamizan','Yusoff','Yusry','Meiyarasan','Danial']
backtomenu = 'y'
while backtomenu == 'y':

    print('1 --> Add new employee name to the list')
    print('2--> Search employee name from the list')
    print('3--> Remove employee name from the list')
    print('4--> Display all the employee name')

    choice = int(input('Enter your choice'))

    if choice == 1:
        name = input('Enter your name')
        name_list.append(name)
        print('Succesfully added')
    elif choice == 2:
        name = input('Enter your name')
        if name in name_list:
            print('{} is available in the list'.format(name))
        else:
            print('{} is not available in the list'.format(name))
    elif choice == 3:
        name = input('Enter your name')
        if name in name_list:
            name_list.remove(name)
            print('{} is succesfully removed from the list'.format(name))
        else:
            print('{} is not in the list'.format(name))
    elif choice == 4:
        print(name_list)
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()



