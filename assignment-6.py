# D20P1
list = []
n = int(input("Enter total number of items stored : "))

for i in range(1, n+1):
    print('Enter {} items:'.format(i))
    ele = int(input())
    list.append(ele)
    str_list = str(list)
    str_list = str_list.replace(',',' ')

print('List of numbers stored in the list : ',str_list)
print('Largest number in the list is',max(list))
print('Smallest number in the list is',min(list))


# D20P2
name_list = ['Ct Wong','Farahanim','Hamizan','Yusoff','Yusry','Meiyarasan','Danial','Khoo']
backtomenu = 1
while backtomenu == 1:

    print('1 --> Add items to the list')
    print('2--> Remove an item from the list')
    print('3--> Searching an item')
    print('4--> Display List items')

    choice = int(input('Enter your choice'))

    if choice == 1:
        name = input('Enter your name')
        name_list.append(name)
        print('Succesfully added')
    elif choice == 2:
        name = input('Enter the names to be removed from the list:')
        if name in name_list:
            name_list.remove(name)
            print('{} name is succesfully removed from the list'.format(name))
        else:
            print('{} is not in the list'.format(name))
    elif choice == 3:
        name = input('Enter the names to be searched:')
        if name in name_list:
            print('Searching names {} is present in the list'.format(name))
        else:
            print('Searching names {} is not present in the list'.format(name))
    elif choice == 4:
        print(name_list)
    else:
        print('Invalid choice')

    backtomenu = int(input('Do you want to continue press 1 otherwise press 0: '))
    if backtomenu == 0:
        print('Thank You')
        exit()
    elif backtomenu != 1:
        print('Rejected')
        exit()

# D20P3
# Admin

employee = {
    'Employee ID' : 'EMP0001',
    'Employee Name' : 'Muhammad Yusri',
    'Employee Address' : 'Jalan Samudra Utara 2, Taman Samudra,',
    'Employee Phone Number' : '010-2349873',
    'Employee Email' : 'yusri@gmail.com',
    'Job title' : 'Programmer',
    'Salary' : '4000.0',
}


backtomenu = 1
while backtomenu == 1:

    print('1 --> Add new books to the library')
    print('2--> Remove the damaged books from the library')
    print('3--> Display all book details')
    print('4--> Display total number of books available in the library')

    choice = int(input('Enter your choice'))

#D20P3

