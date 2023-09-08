s = 1
while s <= 3:
    def read_stdmark():
        global regno,std_name,malay,science,math
        regno = int(input('Enter student ID'))
        std_name = input('Enter student name')
        malay = int(input('Enter malay mark'))
        science = int(input('Enter science mark'))
        math = int(input('Enter math mark'))

    def calculate_mark():
        global total,avg
        total = malay + science + math
        avg = round(total / 3,2)

    def display_result():
        read_stdmark()
        calculate_mark()
        print('Student ID: ', regno)
        print('Student name', std_name)
        print('Malay mark', malay)
        print('Science mark', science)
        print('Math mark', math)
        print('Total mark: {} + {} + {} = {} '.format(malay, science, math, total))
        print('Average mark: ({} + {} + {}) / 3 = {} '.format(malay, science, math, avg))
        if malay >= 50 and science >= 50 and math >= 50:
            result = 'Pass'
            print('Result:', result)
            if avg >= 90:
                print('Grade A+')
            elif avg >= 70:
                print('Grade A')
            elif avg >= 60:
                print('Grade B+')
            elif avg >= 50:
                print('Grade B')
        else:
            result = 'Fail'
            print('Result:', result)
            print('Grade -')
    s += 1
    display_result()
