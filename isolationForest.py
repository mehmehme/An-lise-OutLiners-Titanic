from sklearn.ensemble import IsolationForest
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Seleciona colunas numéricas
X = df[['Age', 'Fare', 'SibSp', 'Parch']].dropna()

# Cria e ajusta modelo
iso = IsolationForest(contamination=0.05, random_state=42)
outliers = iso.fit_predict(X)

# Marca
df['outlier'] = -1
df.loc[X.index, 'outlier'] = outliers

# Filtra apenas os outliers
outliers_detectados = df[df['outlier'] == -1]

# print("Total de outliers encontrados:", len(outliers_detectados))
# print(outliers_detectados[['PassengerId', 'Fare', 'SibSp', 'Parch', 'outlier']])

plt.figure(figsize=(8,6))
plt.scatter(df['Age'], df['Fare'], c=df['outlier'], cmap='coolwarm', alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Outliers detectados pelo Isolation Forest")
plt.show()
