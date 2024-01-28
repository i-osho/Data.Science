import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'age': [25, 30, 22, 35, 28, 40, 26, 32, 29, 31],
    'salary': [60000, 70000, 55000, 80000, 65000, 90000, 62000, 75000, 68000, 82000],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'experience': [2, 5, 1, 8, 3, 12, 4, 7, 6, 9],
    'bonus': [5000, 7000, 3000, 10000, 4500, 12000, 6000, 8000, 7000, 9000]
}

df = pd.DataFrame(data)

df.shape # returns number of rows and columns
df.head() # returns initial entries (5 by default)
df.tail() # returns ending entries (5 by default)
"to print a part of data use index eg. df[2:5]"
df.columns # to print all columns
"df.column_name | df['column_name'] to print a particular row"
df.name
"df[['column1_name', 'column2_name']] to print a multiple rows"
df.describe() # prints statistical information of whole dataset
df.mean() # min() max() mean() std() mode() median()
df[df.age<30]
df[['name', 'age']][df.age==df.age.max()]
df2 = df.set_index('name') # returns a new dataframe with that column as index
df.set_index('name', inplace=True) # inplace=True changes the original dataframe
df2.loc['Alice']
df.reset_index(inplace=True) # resets index to default
"if index is duplicate it will print all the matching entries"


cdata = pd.read_csv('city_data.csv')
df = pd.DataFrame(cdata)
cgroup = df.groupby('city')
for city, city_df in cgroup:
    print(city)
    print(city_df.temperature.mean())
cgroup.get_group('paris')
cgroup.windspeed.median()
