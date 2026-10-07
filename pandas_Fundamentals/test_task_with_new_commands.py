import pandas as pd

df = pd.read_csv("mitarbeiter.csv")


df.head()
df.info()
df.dtypes
df.columns

df["Alter"]
df.loc[0]
df.iloc[0]

df[df["Alter"] > 20]
df.query("Alter > 20")

df["Alter"].mean()
df["Alter"].median()
df["Alter"].min()
df["Alter"].max()
df.describe()

