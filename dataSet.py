import pandas as pd 

file_path = 'CLEAN_FIFA17_official_data.csv'
df = pd.read_csv(file_path)
print(df)

df_new = df['Best Overall Rating'].fillna(0)
print(df_new)
sortByrating =df.sort_values(by='Best Overall Rating', ascending=False)
print(sortByrating.head(10))

print(df.info())
print(df.describe())
print(df.size)
print(sortByrating.tail(10))

