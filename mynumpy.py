# numpy
"""
numpy stands for numerical python.
numpy is a python library user working with the arrays #arrays
numpy methods is use for linear algebra, fourier transformation and matrixes #
numpy is faster than the list
data science # branch of computer science to store the data, use and analyse data for deriving information

"""

# To import numpy
import numpy

# create roll number array
rollnumber = numpy.array([1001,1002,1003,1004,1005,'YUSRY',10.23])

# display array elements
print(rollnumber)

# datatype
print(type(rollnumber))
print(numpy.__version__) # 1.22.4

# Alias name of numpy library
import numpy as np
print(numpy.__version__)
print(np.__version__)

# create array to store student total marks
student_total_mark = np.array([50,90,80,70,80])
print(student_total_mark)

# create array using tuple
student_result = np.array(('pass','pass','pass','pass','pass'))
print(student_result)

# checking number of dimension in the array
print(student_result.ndim)

# Array with the 1 dimension
student_name = np.array(['LeiPin'])
print(student_name)
print(student_name.ndim)

student_name = np.array('LeiPin')
print(student_name)
print(student_name.ndim)

# create array with 2 dimension
numbers = np.array([[1,2],[3,4]])
print(numbers)
print(numbers.ndim)

# create array with 3 dimension
numbers = np.array([[[1,2],[3,4],[5,6]]])
print(numbers)
print(numbers.ndim)

# create array with the single dimension
numbers = np.array ([5,10,15,20,25,30])
print(numbers)

# Access elements from the array using for / while loop
for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(numbers[i])

import numpy as np
numbers = np.array ([5,10,15,20,25,30])
print(numbers)

i = 0
s = len(numbers)
while i<s:
    print(numbers[i])
    i+=1

# Accessing elements from the specific index
#
print(numbers[2]) #15 #fetch second indexed element
print(numbers[-2]) #25 #fetch the negative indexed second element

# slicing
print(numbers[2:5]) #[15 20 25] fetch element from second indexed to forth indexed
print(numbers[:5]) #display from 'zero to 4th' position [5,10,15,20,25,30]
print(numbers[:5]) # starting position 3rd index to end of the index position[ 5 10 15 20 25]
print(numbers[::2]) # [ 5 15 25]
print(numbers[-4:-1])
print(numbers[-5:])
print(numbers[:-4])
print(numbers[::-2])

# Multiple numerical numbers to array elements
print(numbers*2)

# sum of the elements for the array
print(numbers[0]+numbers[1])
s = 0
for i in range(len(numbers)):
    s+=numbers[i]
print('Sum of the elements from array = ',s)

# Datatype of empty array
print(numbers.dtype)

name = np.array(['Yusry','Farith','Afiq'])
print(name.dtype) #<U6 U=unicode 6=number of to hold longers string

studentW = np.array([75.5,80.3,78.9])
print(studentW.dtype) # float64

# Replaced the existing value to array
print(studentW)
studentW[1]=95.5 # [75.5 80.3 78.9]
print(studentW) # [75.5 95.5 78.9]

# copy element one array to another array
employeeW = studentW.copy()
print(employeeW)  # [75.5 95.5 78.9]

# joint the array element
weight=np.concatenate((studentW,employeeW))
print(weight) #[75.5 95.5 78.9 75.5 95.5 78.9]

# Display the shape of the array
matrix1=np.array([[5,10,15,20],[25,30,33,40]])
print(matrix1.shape) # (2,4) 2 row, 4 column

numbers2=np.array([5,10,15,20,25,30,33,40])
print(numbers2.shape) # (8, )

print(numbers2.reshape(4,2))
print(numbers2)

print(numbers2.reshape(3,2))
print(numbers2)

# split the elements
numbers2=np.array([5,10,15,20,25,30,33,40])
split_numbers2 = np.split(numbers2,2)
split_numbers3 = np.split(numbers2,4)
print(numbers2)
print(split_numbers2)
print(split_numbers3)

numbers = np.array([55,100,30,240,20])
print(numbers)
# sort the elements in ascending order
snumbers = np.sort(numbers)
# sort the elements in descending order
print(snumbers[::-1])
# Display string in reverse order
name = 'Lee'
print(name)
print(name[::-1])

# Generate random numbers
#1.
import random
xin = random.randint(1,10)
print(xin)
#2.
import random
xin = random.randint(-10,-1)
print(xin)
#3.
xin = random.random()
print(xin)

# Generate random float number
from numpy import random
xin = random.rand() # rand() method returns the float random number between 0 to 1
print(xin)

# Generate random array
xarray = random.randint(50,size=(10)) # generate 1 dimensional array size 10 containing integers from 0 to 50
print(xarray)

# Generate two dimension of array
xin = random.rand(2,3) # generate of 2-D array 2 rows each row containing 3 random numbers
print(xin)

xin = random.rand(3,4) # generate of 2-D array 3 rows each row containing 4 random numbers
print(xin)

# Generate random numbers from array
xin = random.choice([1,2,3,4,5]) # choice method take array as parameter and randomly return one values from that
print(xin)
xin = random.choice([1,2,3,4,5], size=(2,2)) # generate a 2-D array consists of value in the parameter
print(xin)






