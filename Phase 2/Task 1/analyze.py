import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:/Users/DSK/Desktop/Phase 2/Task 3/dataset - netflix1.csv')

# Data Visualization
# Create different types of graphs for different columns

# Create subplots
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
fig.suptitle("Data Visualization")

# Bar Plot for 'type'
sns.countplot(x='type', data=data, ax=axes[0, 0])
axes[0, 0].set_title('Count of Movies and TV Shows')

# Histogram for 'release_year'
sns.histplot(data['release_year'], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Release Years')

# Box Plot for 'release_year'
sns.boxplot(y='release_year', data=data, ax=axes[0, 2])
axes[0, 2].set_title('Box Plot of Release Year')

# Count Plot for 'rating'
sns.countplot(x='rating', data=data, order=data['rating'].value_counts().index, ax=axes[0, 3])
axes[0, 3].set_title('Count of Ratings')
axes[0, 3].tick_params(axis='x', rotation=90)

# Count Plot for 'country'
sns.countplot(x='country', data=data, order=data['country'].value_counts().iloc[:10].index, ax=axes[1, 0])
axes[1, 0].set_title('Top 10 Countries')
axes[1, 0].tick_params(axis='x', rotation=90)

# Box Plot for 'duration'
sns.boxplot(x='type', y='release_year', data=data, ax=axes[1, 1])
axes[1, 1].set_title('Box Plot of Release Year by Type')
axes[1, 1].tick_params(axis='x', rotation=90)

# Customized plot (add your own code here)
# Example: Pie Chart for 'type'
type_counts = data['type'].value_counts()
axes[1, 2].pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
axes[1, 2].set_title('Distribution of Movie vs TV Show')

# Remove empty subplots
fig.delaxes(axes[1, 3])

# Display all plots
plt.tight_layout()
plt.show()


