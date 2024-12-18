import pandas as pd
import random
from datetime import datetime, timedelta

# Generate random employee data
def generate_data(n):
    data = {
        'id': range(1, n + 1),
        'name': [f'Name_{i}' for i in range(1, n + 1)],
        'age': [random.randint(18, 80) for _ in range(n)],
        'city': [random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']) for _ in range(n)],
        'salary': [random.randint(30000, 120000) for _ in range(n)],
        'join_date': [(datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') for _ in range(n)],
    }
    return pd.DataFrame(data)

# Generate and save the data as a CSV file
df = generate_data(100)
df.to_csv('employee_data.csv', index=False)

# Load the data from CSV
df_loaded = pd.read_csv('employee_data.csv')
print(df_loaded.head())  # Display first few rows of the loaded data


import pandas as pd

# Load the data from CSV
df = pd.read_csv('employee_data.csv')

# Display the first few rows of the dataset to understand its structure
print(df.head())


import matplotlib.pyplot as plt
import seaborn as sns

# Query 1: Average Salary by City
average_salary = df.groupby('city')['salary'].mean()

# Plotting
plt.figure(figsize=(10, 6))
average_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary by City')
plt.xlabel('City')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()

# Query 2: Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['salary'], kde=True, color='purple')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Query 3: Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], kde=True, color='green')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Query 4: Salary vs. Age (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='salary', data=df, color='blue')
plt.title('Salary vs. Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Query 5: Number of Employees in Each City
employee_count = df['city'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
employee_count.plot(kind='bar', color='orange')
plt.title('Number of Employees in Each City')
plt.xlabel('City')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.show()


plt.savefig('average_salary_by_city.png')
