# Loop - repeatly execute statement until certain condition is true
# create a python program to display name in python
name = input('Enter your name')
print(name)
print(name)
print(name)
print(name)
print(name)

print(name * 5)
print(name + '\n' + name + '\n' + name + '\n' + name + '\n' + name)

# while-loop
"""
3 statement needed
1. Initialize control variable
2. check the condition
3. update the control variable
"""

i = 1  # initialize control variable
while i <= 5:  # check the condition
    print('Fudhail')  # body of loop
    i = i + 1  # update the control variable

# display number from 1 to 10

x = 1
while x <= 10:
    print(x)
    x = x + 1  # or x += 1

y = 10
while y >= 1:
    print(y)
    y = y - 1  # or y -= 1

# even number
f = 2
while f <= 50:
    print(f)
    f = f + 2  # or f += 2

# odd number
p = 1
while p <= 50:
    print(p)
    p = p + 2  # or p += 2

# fibonacci

f = 0
s = 1
t = f + s
print(f)
print(s)
series = 3

while series <= 10:
    t = f+s
    print(t)
    f = s
    s = t
    series += 1


# Display multiplication table
mul = 4
num = 1

while num <= 20:
    p = str(num * mul)
    print(num, 'X 4 = ', p)
    num = num + 1

i=1
while i<= 5: # outer loop
    j=1
    while j<=i: # inner loop
        print(j,end=' ')
        j+=1
    print()
    i+=1

    i = 1
    while i <= 5:  # outer loop
        j = 1
        while j <= i:  # inner loop
            print('*', end=' ')
            j += 1
        print()
        i += 1

        i = 1
        while i <= 5:  # outer loop
            j = 1
            while j <= i:  # inner loop
                print(i, end=' ')
                j += 1
            print()
            i += 1

            # break statement - used stop the execution of corresponding loop
            i = 1
            while i <= 5:
                if i == 3:
                    break # stop the execution
                print(i)
                i = i + 1
            print('End of program')

            # continue statement - used to skip part of execution
            i = 0
            while i <= 5:
                i = i + 1
                if i==3:
                    continue
                print(i)

            # for loop
            for i in range(1,6):
                print(i)

            # for loop
            for i in range(1,11,2):
                print(i)

            # for loop
            for i in range(1, 51, 4):
                print(i)

            # nested for loop
            for i in range(1,6):
                for j in range(1,i+1):
                    print(j,end=' ')
                print()

            # for loop
            for i in range(1,6):
                if i == 3:
                    break
                print(i)

            # for loop
            for i in range (1,6):
                if i == 3:
                    continue
                print(i)
