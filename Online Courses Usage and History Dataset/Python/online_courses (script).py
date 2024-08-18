# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
data = pd.read_csv(r"C:\Users\ASUS\Desktop\Machine Learning\Pratice Projects\Online Courses Usage and History Dataset\Excel\online_courses_uses.csv")
data.head(1)

# %%
category_counts = data['Category'].value_counts()
category_counts

# %%
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Course Categories')
plt.xlabel('Category')
plt.ylabel('Number of Courses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() 

# %%
plt.figure(figsize=(10, 6))
plt.hist(data['Duration (hours)'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Course Durations')
plt.xlabel('Duration (hours)')
plt.ylabel('Number of Courses')
plt.grid(True)
plt.show()

# %%
plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Duration (hours)', data=data, palette='Set3')
plt.title('Course Duration by Category')
plt.xlabel('Course Category')
plt.ylabel('Duration (hours)')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.show()

# %%
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Enrolled_Students', y='Completion_Rate (%)', data=data, s=70, alpha=0.6)
plt.title('Enrollment vs. Completion Rate')
plt.xlabel('Number of Enrolled Students (Log Scale)')
plt.ylabel('Completion Rate (%)')
plt.xscale('log')  
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# %%
avg_prices = data.groupby('Category')['Price ($)'].mean().sort_values()
plt.figure(figsize=(12, 8))
avg_prices.plot(kind='bar', color='green', edgecolor='black')
plt.title('Average Course Prices by Category')
plt.xlabel('Course Category')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45, ha='right')  
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# %%
courses_per_platform = data['Platform'].value_counts()
plt.figure(figsize=(12, 8))
courses_per_platform.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Courses by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Courses')
plt.xticks(rotation=45, ha='right') 
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# %%
pivot_data = data.pivot_table(index='Category', columns='Platform', values='Enrolled_Students', aggfunc='sum').fillna(0)
ax = pivot_data.plot(kind='bar', stacked=False, figsize=(14, 8), colormap='tab20')
plt.title('Total Number of Enrolled Students by Category')
plt.xlabel('Course Category')
plt.ylabel('Total Enrolled Students')
plt.xticks(rotation=45, ha='right') 
ax.get_yaxis().set_visible(False)
plt.tight_layout()
plt.show()

# %%
data.head()

# %%
price_analysis = data.groupby(['Category', 'Platform'])['Price ($)'].mean().unstack()
plt.figure(figsize=(12, 8))
price_analysis.plot(kind='bar', figsize=(12, 8))
plt.title('Average Price by Category and Platform')
plt.xlabel('Category')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45)
plt.legend(title='Platform')
plt.tight_layout()
plt.show()

# %%
rating_analysis = data.groupby(['Category', 'Platform'])['Rating (out of 5)'].mean().unstack()
plt.figure(figsize=(12, 8))
rating_analysis.plot(kind='bar', figsize=(12, 8))
plt.title('Average Rating by Category and Platform')
plt.xlabel('Category')
plt.ylabel('Average Rating (out of 5)')
plt.xticks(rotation=45)
plt.legend(title='Platform')
plt.tight_layout()
plt.show()

# %%
completion_analysis = data.groupby(['Category', 'Platform'])['Completion_Rate (%)'].mean().unstack()
plt.figure(figsize=(12, 8))
completion_analysis.plot(kind='bar', figsize=(12, 8))
plt.title('Average Completion Rate by Category and Platform')
plt.xlabel('Category')
plt.ylabel('Average Completion Rate (%)')
plt.xticks(rotation=45)
plt.legend(title='Platform')
plt.tight_layout()
plt.show()


