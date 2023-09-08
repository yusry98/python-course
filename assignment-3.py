# D16P1
# To get Total of All Subjects
science_mark=int(input('Enter Science mark: '))
english_mark=int(input('Enter English mark: '))
maths_mark = int(input('Enter Maths mark: '))
total = science_mark + english_mark + maths_mark
print('Total of all subjects is = ', total)

# To deduct marks for late Assignment Submission
mark = int(input('Enter your mark'))
deduct_mark_late = 5
new_mark = mark - deduct_mark_late
print(new_mark)

# To find the percentage of the mark
full_mark = 300
final_mark = 240
marks_percentage = final_mark / full_mark * 100
print(marks_percentage,'%')

# To divide roll numbers in even and odd list
student_rollno = int(input('Enter student roll number: '))
if student_rollno % 2 == 0:
    print('Student roll number is in even list')
else:
    print('Student roll number is in odd list')

# To round off total marks
final_mark = 240
total_no_subject = 3
round_off = 240 // 3
print('After round off: ',round_off)


# D16P2

# To get Total of All Subjects
science_mark=int(input('Enter Science mark: '))
english_mark=int(input('Enter English mark: '))
maths_mark = int(input('Enter Maths mark: '))
total = (science_mark.__add__(english_mark)).__add__(maths_mark)
print('Total of all subjects is = ', total)

# To deduct marks for late Assignment Submission
mark = int(input('Enter your mark'))
deduct_mark_late = 5
new_mark = mark.__sub__(deduct_mark_late)
print(new_mark)

# To find the percentage of the mark
full_mark = 300
final_mark = 240
marks_percentage = (final_mark.__truediv__(full_mark)).__mul__(100)
print(marks_percentage,'%')

# To divide roll numbers in even and odd list
student_rollno = int(input('Enter student roll number: '))
if student_rollno.__mod__(2) == 0:
    print('Student roll number is in even list')
else:
    print('Student roll number is in odd list')

# To round off total marks
final_mark = 240
total_no_subject = 3
round_off = 240 .__floordiv__(3)
print('After round off: ',round_off)

# D16P3
mark = int(input('Enter student mark'))

if mark < 50:
    print('Mark is lower than 50')
elif mark > 50:
    print('Mark is higher than 50')
elif mark == 50:
    print('Student name : Yusry')

# D16P4
mark = int(input('Enter exam mark:'))
pass_exam = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
if mark in pass_exam:
    print('Result : Pass')
else:
    print('Result : Fail')

# D16P5
mark = int(input('Enter exam mark:'))
pass_exam = [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
if mark in pass_exam:
    A = pass_exam
    if A is pass_exam:
        print('Result : Pass')
        print('Grade: A')
else:
    print('Result : Fail')
    print('Grade: -')
