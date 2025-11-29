import pandas as pd 
   
# df = pd.DataFrame() 
# print(df)
data={'Name':['Geeks', 'For', 'Geeks', 'is'] ,
'Age':[30,33,56,87] ,
'City':['delhi', 'mumbai', 'amravati', 'akola' ] 
}

print(data)
df = pd.DataFrame(data)
print(df)
#typesOfData 
print(type(data))

#addNewCol
df['Score'] = [86,84,32,21]
print(df)

#Updtate the coloum 
df["Score"] = df["Score"]+5

print(" updated data ")
print(df)

# print(df.mean("columns"))
 # drop the data 
df = df.drop('City',axis=1)
print(df)

#sort Ascending 
Sort = df.sort_values(by='Age')
print(Sort)

#sort Descending  by values 
Sort1 = df.sort_values(by='Age', ascending=False)
print(Sort1)



#sort Descending  by indexs
sort_Index = df.sort_index(ascending=False)
print(sort_Index)

#Renaming Coloum 
df=df.rename(columns={'Score':'Final_Score'})
print(df)

#data with nun values
data_nun ={'Name':['Geeks', 'For', 'Geeks', 'is'] ,
'Age':[30,None,56,None] ,
'City':['delhi', 'mumbai', 'amravati', 'akola' ] 
}

print(data_nun)
data_with_nun = pd.DataFrame(data_nun)
data_with_nun['Age']= data_with_nun['Age'].fillna(data_with_nun['Age'].mean())
print(data_with_nun)

#changes to  zero 
data_zeronun ={'Name':['Geeks', 'For', 'Geeks', 'is'] ,
'Age':[30,None,56,None] ,
'City':['delhi', 'mumbai', 'amravati', 'akola' ] 
}
print(data_zeronun)
zeroData = pd.DataFrame(data_zeronun)
zeroData['Age']=zeroData['Age'].fillna(0)

print(zeroData)

# drop the coloum  
dfDrop = pd.DataFrame(data_zeronun)
dataDroped = dfDrop.dropna()
print(dataDroped)