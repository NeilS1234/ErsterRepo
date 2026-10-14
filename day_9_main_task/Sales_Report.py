import pandas as pd

# Load CSV file
df = pd.read_csv("C:/Users/2918965/OneDrive - EDEKA/Desktop/ErsterRepo/day_9_main_task/sales_data.csv")

# Calculated column
df["Preis_pro_Stueck"] = df["Umsatz"] / df["Menge"]

print("\n--- SALES DATA ---")
print(df)

# Group by two categories
print("\n--- REVENUE BY REGION AND CATEGORY ---")
gruppen = df.groupby(
    ["Region", "Kategorie"]
)["Umsatz"].sum()
print(gruppen)

# Totals and averages
print("\n--- TOTALS AND AVERAGES ---")
bericht = df.groupby(
    ["Region", "Kategorie"]
)["Umsatz"].agg(["sum", "mean"])
print(bericht)

# Highest and lowest performing groups
print("\n--- BEST AND WORST GROUP ---")
beste_gruppe = gruppen.idxmax()
schlechteste_gruppe = gruppen.idxmin()

print("Best group:", beste_gruppe)
print("Highest revenue:", gruppen.max(), "Euro")

print("Worst group:", schlechteste_gruppe)
print("Lowest revenue:", gruppen.min(), "Euro")

# Pivot table
print("\n--- PIVOT TABLE ---")
pivot = pd.pivot_table(
    df,
    values="Umsatz",
    index="Region",
    columns="Kategorie",
    aggfunc="sum",
    fill_value=0
)
print(pivot)

# Overall report
print("\n--- OVERALL REPORT ---")
print("Total revenue:", df["Umsatz"].sum(), "Euro")
print("Average revenue:", df["Umsatz"].mean(), "Euro")
print("Total quantity sold:", df["Menge"].sum())