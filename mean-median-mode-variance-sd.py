#Handling big data set
import numpy
x = numpy.random.uniform(0.0,5.0,250)
print('Random numbers:\n',x)
print('Total number of random numbers is:',len(x))

#Histogram
#To visualize the data set we can draw a histogram with the data we collected
import matplotlib.pyplot as plt
import numpy

x = numpy.random.uniform(0.0,5.0,250)
print(x)
plt.hist(x,5)
plt.show()

# Create an array with 100000 random numbers, and display them using a histogram with 100 bars
import matplotlib.pyplot as plt
import numpy

x = numpy.random.uniform(0.0,5.0,100000)
print(x)
plt.hist(x,100)
plt.show()

# Mean, median, mode, variance, and standard deviation
# Mean is average value
# example 1
import numpy as np
x = [99,86,87,88,111,86,103,87,94,78,77,85,86]
xmean = np.mean(x) #(99+86+87+88+111+86+103+87+94+78+77+85+86)/13
xsum = np.sum(x) # 99+86+87+88+111+86+103+87+94+78+77+85+86
print(xmean)
print(xsum)

# example 2
import numpy as np
s = [50,65,70,80,85,98,100,120]
smean = np.mean(s)
print(smean)
s_sum = np.sum(s)
print(s_sum)

# median is value at middle position after sorting the list
# car speed
import numpy as np
carspeed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
xsort = np.sort(x)
print(xsort)
xmedian = np.median(carspeed)
print(xmedian)
# student mark
import numpy as np
student_mark = [50,65,70,80,85,100,98,120]
studentmedian = np.median(student_mark)
print(studentmedian)

# Mode is the value that appear the most
# car speed
from scipy import stats
carspeed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
carmode = stats.mode(carspeed)
print(carmode)
# student mark
from scipy import stats
student_mark = [50,65,70,80,85,100,98,120]
studentmarkmode = stats.mode(student_mark)
print(studentmarkmode)


# variance indicate how spread out the values are
x = [10,20,30]
xmean = 20.0
xvariance = ((10 - 20.0)**2 + (20-20.00)**2 + (30-20.0)**2) / 3
print(xvariance)
xvar = np.var(x)
print(xvar)
# Standard deviation describe how the value spread out
# Low standard deviation most of the value is close to mean(average value)
# High standard deviation the values spread out of the wider range
xstd = np.std(x)
print(xstd)

# Employee salary
employeesalary = [1500,3000,4200,2090,1200,3100,1500,2000,3120]
employeesalarymean = np.mean(employeesalary)
employeesalarymedian = np.median(employeesalary)
employeesalarymode = stats.mode(employeesalary)
employeesalaryvariance = np.var(employeesalary)
employeesalarystd = np.std(employeesalary)
print('Employee salary mean\t',employeesalarymean)
print('Employee salary median\t',employeesalarymedian)
print('Employee salary mode\t',employeesalarymode)
print('Employee salary variance\t',employeesalaryvariance)
print('Employee salary standard deviation\t',employeesalarystd)

# Normal data distribution
import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(5.0,1.0,100000)
print(x)
plt.hist(x,100)
plt.show()

# Scatter Plot
# A scatter plot is a diagram where each value in the data set is represented by a dot.
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [30,60,87,70,100,86,95,87,25,78,77,45,86]
plt.scatter(x,y)
plt.show()

x = numpy.random.normal(5.0,1.0,1000)
y = numpy.random.normal(10.0,2.0,1000)
print(x)
plt.scatter(x,y)
plt.show()

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # Ages of car
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # Milage
print(stats.linregress(x,y))
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
