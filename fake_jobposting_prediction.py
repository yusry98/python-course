# Import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# To read csv file
data = pd.read_csv('fake_job_postings.csv')
print(data)

# To display top 5 rows
data_top = data.head()
print(data_top)

# To view data info
data_info = data.info()
print(data_info)

# To view column
data_columns = data.columns
print(data_columns)

# Count NaN on entire DataFrame
count_nan = data.isnull().sum()
print(count_nan)

# To remove columns from DataFrame
data.drop(['job_id' , 'salary_range' , 'telecommuting' , 'has_company_logo' , 'has_questions'] , axis = 1,inplace = True)

# To return a tuple representing the dimensionality of the DataFrame
data_shape = data.shape
print(data_shape) # (17880, 13)

# To replaces the NULL values
data.fillna(' ',inplace=True) # fillna() method returns a new DataFrame object unless the inplace parameter is set to True

# Proportion of Fraudulent Job Posting - Pie Chart
labels = 'Fake' ,'Real'

sizes = [data.fraudulent[data['fraudulent'] == 1].count() ,data.fraudulent[data['fraudulent'] == 0].count()]
explode =(0,0.1)

fig1 ,ax1 = plt.subplots(figsize =(12,9))
ax1.pie(sizes ,explode =explode, labels = labels, autopct ='%1.1f%%',startangle =180)

ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Proportion of Fraudulent Job Posting" ,size =7)
plt.show()

# Visualize Job postings by countries
def split(location):
    l = location.split(',')
    return l[0]

data['country'] =data.location.apply(split)

# To returns the number of unique values in column country
data['country'].nunique()

# To returns a series containing the counts of unique values
data['country'].value_counts()

# Country-wise job posting - Bar Graph
country =dict(data.country.value_counts()[:11])

del country[' ']
plt.figure(figsize=(7,4))

plt.title('Country-wise Job Posting',size=14)
plt.bar(country.keys(),country.values())

plt.xlabel('Name of Country')
plt.ylabel('Number of Jobs')

# Visualize Job posting by Experience - Bar Graph
experience =dict(data.required_experience.value_counts()[:11])

del experience[' ']
plt.figure(figsize=(12,9))

plt.title('Experience-wise Job Posting',size=14)
plt.bar(experience.keys(),experience.values())

plt.xlabel('Experience')
plt.ylabel('Number of Jobs')

# Visualize Job posting by Department
department1 =dict(data.department.value_counts()[:11])

del department1[' ']
plt.figure(figsize=(15,9))

plt.title('Department-wise Job Posting',size=20)
plt.bar(department1.keys(),department1.values())

plt.xlabel('Department')
plt.ylabel('Number of Jobs')

# To find the fake job titles
data.title.value_counts()[:11]
# Fake job titles:
data[data.fraudulent == 1].title.value_counts()[:11]
# real job titles:
data[data.fraudulent == 0].title.value_counts()[:11]

# Check the frequency of Word in datsets
data['text'] = data['title'] + ' '+ data['location'] + ' ' + data['department'] + ' ' + data['company_profile'] + ' '+ data['description'] + ' ' + data['requirements'] + ' ' + data['benefits'] + ' ' + data['industry']
from wordcloud import WordCloud
all_words = ' '.join([text for text in data['text']])
wordcloud = WordCloud(width = 600 ,height = 300, max_font_size = 120).generate(all_words)
plt.figure(figsize =(12,9))

plt.imshow(wordcloud)
plt.show()

# frequency of word in real posting of jobs
real_post = ' '.join([text for text in data['text'][data['fraudulent']==0]])
wordcloud1 = WordCloud(width = 600 ,height = 300, max_font_size = 120).generate(real_post)
plt.figure(figsize =(12,9))

plt.imshow(wordcloud1)
plt.show()

# frequency of word in fake job postings
fake_post = ' '.join([text for text in data['text'][data['fraudulent'] == 1]])
wordcloud2 = WordCloud(width = 600 ,height = 300, max_font_size = 120).generate(fake_post)
plt.figure(figsize =(12,9))

plt.imshow(wordcloud2)
plt.show()



