# to write contents to the file
try:
    f = open('patient_lis','w')
finally:
    f.close()

# To read contents from file
try:
    f = open('patient_list','r')
    print(f.read())
finally:
    f.close()

# Replace previous read file coding
with open('mytxt') as fp:
    print(fp.read())

# Merging two file
str1=str2 =" "

# To read data from f1 file and store it in str1 variable
with open('patient_list') as fp:
    str1 = fp.read()

print('Content from f1 file\n',str1)

# To read data from f2 file and store it in str2 variable
with open('mytxt') as fp:
    str2 = fp.read()
print('\nContent from f2 file\n', str2)

str3 = str1+'\n' + str2 # Combine two string and make it one
print('\nValue from str3 variable\n', str3)

# To write combined string to f3
with open ('f3','w') as fp:
    fp.write(str3)

# To write combined string to f3
with open('f3') as fp:
    print('\nMerging file contents\n', fp.read())






