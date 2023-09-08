# nested dictionary
employee = {
    'Employee ID' : 'EMP0001',
    'Employee Name' : 'Muhammad Yusri',
    'Employee Address' : 'Jalan Samudra Utara 2, Taman Samudra,',
    'Employee Phone Number' : '010-2349873',
    'Employee Email' : 'yusri@gmail.com',
    'Job title' : 'Programmer',
    'Salary' : '4000.0',
}

employee2 = {
    'Employee ID' : 'EMP0002',
    'Employee Name' : 'Farith Amer',
    'Employee Address' : '11 Jln Ss2/67 Ss2 Petaling Jaya',
    'Employee Phone Number' : '014-5542211',
    'Employee Email' : 'farithamer@gmail.com',
    'Job title' : 'Web Designer',
    'Salary' : '3500.0',
}

employee3 = {
    'Employee ID' : 'EMP0003',
    'Employee Name' : 'Wan Afiq',
    'Employee Address' : 'Plot 22, Tupai Light Industrial Area',
    'Employee Phone Number' : '013-4556998',
    'Employee Email' : 'wanafiq@gmail.com',
    'Job title' : 'IT Technician',
    'Salary' : '3000.0',
}

employee4 = {
    'Employee ID' : 'EMP0004',
    'Employee Name' : 'Irfan Isa',
    'Employee Address' : '52 1 Jln Usj 9/5P Taman Seafield Jaya Petaling Jaya',
    'Employee Phone Number' : '019-77855966',
    'Employee Email' : 'irfanisa@gmail.com',
    'Job title' : 'IT Executive',
    'Salary' : '5500.0',
}

employee5 = {
    'Employee ID' : 'EMP0005',
    'Employee Name' : 'Hairul Penyu',
    'Employee Address' : 'Jalan Permatang Gedong, Taman Sejati Indah,',
    'Employee Phone Number' : '012-55441123',
    'Employee Email' : 'hairulpenyu.com',
    'Job title' : 'Database Administrator',
    'Salary' : '4000.0',
}

emp_record = {
    'Employee1':employee,
    'Employee2':employee2,
    'Employee3':employee3,
    'Employee4':employee4,
    'Employee5':employee5,
}

print(emp_record['Employee1'])
print(emp_record['Employee2'])
print(emp_record['Employee3'])
print(emp_record['Employee4'])
print(emp_record['Employee5'])

print(employee)
backtomenu = 'y'
while backtomenu == 'y':

    print('1--> Access employee information from dictionary')
    print('2--> Check employee available or not')
    print('3--> Display all the values from dictionary')
    print('4--> Remove item from dictionary')
    print('5--> Remove all item from dictionary')
    print('6--> Length of dictionary')
    print('7--> Remove memory from dictionary')

    choice = int(input('Enter your choice'))

    if choice == 1:
        key = input('Enter employee to be search')
        if key in emp_record:
            x = emp_record.get(key)
            print(x)
        else:
            print(key, 'not in the dictionary')
    elif choice == 2:
        key = input('Enter employee to be check')
        if key in emp_record:
            print(key, 'is available')
        else:
            print(key, 'is not available')
    elif choice == 3:
        x = emp_record.values()
        print(x)
    elif choice == 4:
        key = input('Enter employee to be remove')
        if key in emp_record:
            emp_record.pop(key)
            print(key, 'removed successfully')
        else:
            print(key, 'not in the dictionary')
    elif choice == 5:
        emp_record.clear()
        print('Items removed successfully')
    elif choice == 6:
        print('Length of dictionary is' ,len(emp_record))
    elif choice == 7:
        del emp_record
        print('Successfully removed memory from dictionary')
    else:
        print('Invalid choice')

    backtomenu = input('Do you want to continue press y otherwise press n: ')
    if backtomenu == 'n':
        print('Thank You')
        exit()
    elif backtomenu != 'y':
        print('Rejected')
        exit()