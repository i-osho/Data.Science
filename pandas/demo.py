import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Age': [25, 30, 22, 35, 28, 40, 26, 32, 29, 31],
    'Salary': [60000, 70000, 55000, 80000, 65000, 90000, 62000, 75000, 68000, 82000],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Experience': [2, 5, 1, 8, 3, 12, 4, 7, 6, 9],
    'Bonus': [5000, 7000, 3000, 10000, 4500, 12000, 6000, 8000, 7000, 9000]
}

df = pd.DataFrame(data)

df.shape # returns number of rows and columns
df.head() # returns initial entries (5 by default)
df.tail() # returns ending entries (5 by default)
# to print a part of data use index eg. df[2:5]
df.columns # to print all columns
# df.column_name to print a particular row
df.Name