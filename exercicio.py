import pandas as pd
import re

df = pd.read_csv("train.csv")


print("\n Dados Inconsistentes:")
inc = df[(df['Age'] < 0 ) | (df['Age'] > 120)] 
# não há idades negativas ou altissimas

inc2 = df[~df['Embarked'].isin(["C", "Q", "S"])] # não(~) isin() 
#há dois passageiros que foram embarcados com NaN
# 61            62                        Icard, Miss. Amelie      NaN
# 829          830  Stone, Mrs. George Nelson (Martha Evelyn)      NaN

inc3 = df[~df['Sex'].isin(['male','female'])]
#não há pessoas de sexo fora de masculino e feminino

print(inc[['PassengerId','Name','Sex']].head())

print("\n Dados Redundantes:")
print(df[['PassengerId','Name']].duplicated().sum())
# não há id's ou nomes redundantes

print("\n Dados Incompletos:")
print(df[['Name','Age','Sex','Cabin']].isna().sum())
# Existem 177 idades incompletas e 687 cabines incompletas

print("\n Dados Ruidosos:")
print(df[['Name','Ticket','Cabin']])
# há várias alternâncias nesses 3 dados

df["Title"] = df["Name"].apply(lambda x: re.search(r",\s*([^\.]*)\.", x).group(1).strip())
print(df["Title"].value_counts())
title_map = {
    "Mlle": "Miss",
    "Ms": "Miss",
    "Mme": "Mrs",
    "Lady": "Royalty",
    "Countess": "Royalty",
    "Capt": "Officer",
    "Col": "Officer",
    "Major": "Officer",
    "Dr": "Officer",
    "Rev": "Officer",
    "Sir": "Royalty",
    "Don": "Royalty",
    "Jonkheer": "Royalty"
}
df["Title"] = df["Title"].replace(title_map)

# temos:
# Title
# Mr              517
# Miss            182
# Mrs             125
# Master           40
# Dr                7
# Rev               6
# Col               2
# Mlle              2
# Major             2
# Ms                1
# Mme               1
# Don               1
# Lady              1
# Sir               1
# Capt              1
# the Countess      1
# Jonkheer          1

df["TicketPrefix"] = df["Ticket"].str.extract(r"([A-Za-z./]+)")
df["TicketNumber"] = df["Ticket"].str.extract(r"(\d+)")
print(df["TicketPrefix"])
print(df["TicketNumber"])
#separamos as letras dos números
  
print(df["Cabin"].notna().sum()) 


