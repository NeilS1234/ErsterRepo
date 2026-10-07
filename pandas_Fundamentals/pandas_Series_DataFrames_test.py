import pandas as pd

noten = pd.Series([1, 2, 3, 2, 1])

print(noten)


df = pd.DataFrame({
    "Name": ["Anna", "Ben", "Chris"],
    "Alter": [20, 25, 22]
})

df["Alter"]

df[["Name", "Alter"]]

df = pd.read_csv("mitarbeiter.csv")

df.loc[0]
df.loc[0, "Name"]

df.iloc[0]
df.iloc[0, 1]

df[df["Alter"] > 20]
df[df["Alter"] == 20]
df[df["Alter"] < 25]

df.query("Alter > 20")
df[df["Alter"] > 20] 

df["Alter"].mean()
df["Alter"].median()
df["Alter"].min()
df["Alter"].max()
df["Alter"].sum()
df["Alter"].count()
df["Alter"].std()
df.describe()

