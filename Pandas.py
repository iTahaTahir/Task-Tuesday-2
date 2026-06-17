import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


filepath = "dirty_cafe_sales.csv"


# LOADING DATASET FROM READIONG CSV FILE
df = pd.read_csv(filepath)

# Printing information on dataset
df.info()

# printing number of duplicates
print(f"\033[91mNumber of duplicates: {df.duplicated().sum()} \033[0m")

#printing number of missing values
print(f"\033[93mNumber of missing values:\033[0m \n{df.isnull().sum()} ")
print(f"\033[93mTotal number of missing values: {df.isnull().sum().sum()} \033[0m")

#fixing the column names
df.columns = df.columns.str.strip()


# fixing types of dataset
print(f"\033[92mData types before fixing:\033[0m \n{df.dtypes}")

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

print(f"\033[92mData types after fixing:\033[0m \n{df.dtypes}")
print(f"\033[91mMissing rows: \033[0m \n {df[df.isnull().any(axis=1)]}")

#Handing values that are a bit dirty and impute them with nan/None

label_columns = []
for column in df.columns:
    if df[column].dtype == 'str':
        label_columns.append(column)

for columns in label_columns:
    frequencies = df[columns].value_counts(normalize=True)
    bad_labels = frequencies[frequencies < 0.06].index  
    if columns != 'Transaction ID':  
        df[columns] = df[columns].replace(bad_labels, pd.NA)

print(f"\033[93mTotal number of missing values: {df.isnull().sum().sum()} \033[0m")

#Handling missing values
mode_item = df['Item'].mode()[0]
print(f"\033[93mMost frequent item: {mode_item} \033[0m")
df['Item'] = df['Item'].fillna(mode_item)
df['Price Per Unit'] = df['Price Per Unit'].fillna(df['Price Per Unit'].mean())
df['Total Spent'] = df['Total Spent'].fillna(df['Total Spent'].mean())
mode_Payment_method  = df['Payment Method'].mode()[0]
print(f"\033[93mMost frequent payment method: {mode_Payment_method} \033[0m")
df['Payment Method'] = df['Payment Method'].fillna(mode_Payment_method)
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
df['Transaction Date'] = df['Transaction Date'].fillna(df['Transaction Date'].mean())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())

print(f"\033[92mNumber of missing values after fixing:\033[0m \n{df.isnull().sum()} ")

# since we do not need transaction Id for training
df.drop('Transaction ID', axis=1, inplace=True)

#Dataset Shape
print(f"\033[92mDataset shape: {df.shape} \033[0m")
print(f"\033[92mDataset head:\033[0m \n{df.head()}")
print(f"\033[92mDataset Statistical description:\033[0m \n{df.describe()}")

# Most popular values and their frequenecies
print(f"\033[93mMost popular items:\033[0m \n{df['Item'].value_counts()}")
print(f"\033[93mMost popular payment methods:\033[0m \n{df['Payment Method'].value_counts()}")
print(f"\033[93mMost popular locations:\033[0m \n{df['Location'].value_counts()}")

#visualizing the distribution of total spent
plt.figure(figsize=(10,6))
sns.histplot(
    df['Total Spent'], 
    kde=True,
    bins = 30
    )
plt.title('Distribution of Total Spent')
plt.xlabel('Total Spent')
plt.ylabel('Frequency')


#visualizing Location 
plt.figure(figsize=(10,6))
plt.pie(
    df['Location'].value_counts(),
    colors = sns.color_palette('pastel'),
    autopct='%1.1f%%',
    startangle = 140
    )
plt.title('Distribution of Locations')
plt.legend(df['Location'].value_counts().index, loc='best')
plt.show()


#base path
dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(dir, "dirty_cafe_sales.csv")

#loading another dataset for joining
df2 = pd.read_csv(filepath)


#joining 
df_merged = pd.merge(df,df2,on='Item',how='inner')
print(f"\033[92mMerged dataset head:\033[0m \n{df_merged.head()}")
print(f"\033[92mMerged dataset shape: \033[0m {df_merged.shape}")
print(f"\033[92mMerged dataset info:\033[0m \n")
df_merged.info()