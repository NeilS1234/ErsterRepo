import requests
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Folder for the results
Path("output").mkdir(exist_ok=True)


# Download data from the World Bank
def get_data(indicator, name):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator}"

    params = {
        "format": "json",
        "date": "2000:2023",
        "per_page": 20000
    }

    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()[1]

    df = pd.DataFrame(data)

    df["country"] = df["country"].apply(
    lambda x: x["value"] if isinstance(x, dict) else x
)

    df = df[["countryiso3code", "country", "date", "value"]]
    df.columns = ["code", "country", "year", name]

    df["year"] = pd.to_numeric(df["year"])
    df[name] = pd.to_numeric(df[name])

    return df[df["code"].str.len() == 3]


# Get both datasets
gdp = get_data("NY.GDP.PCAP.CD", "gdp")
life = get_data("SP.DYN.LE00.IN", "life")

# Join the datasets by country and year
data = pd.merge(
    gdp,
    life[["code", "year", "life"]],
    on=["code", "year"]
)

data = data.dropna(subset=["gdp", "life"])
data = data[data["gdp"] > 0]

# Save the joined data
data.to_csv("output/merged_dataset.csv", index=False)

# Use the latest year with data
year = int(data["year"].max())
latest = data[data["year"] == year]


# Chart 1: GDP and life expectancy
plt.figure()
plt.scatter(latest["gdp"], latest["life"])
plt.xscale("log")
plt.xlabel("GDP per person (US dollars)")
plt.ylabel("Life expectancy (years)")
plt.title("GDP and Life Expectancy")
plt.tight_layout()
plt.savefig("output/chart1.png")
plt.close()


# Chart 2: Life expectancy over time
life_by_year = data.groupby("year")["life"].median()

plt.figure()
plt.plot(life_by_year.index, life_by_year.values, marker="o")
plt.xlabel("Year")
plt.ylabel("Life expectancy (years)")
plt.title("Life Expectancy Over Time")
plt.tight_layout()
plt.savefig("output/chart2.png")
plt.close()


# Chart 3: Ten countries with the highest GDP
top10 = latest.nlargest(10, "gdp").sort_values("gdp")

plt.figure()
plt.barh(top10["country"], top10["gdp"])
plt.xlabel("GDP per person (US dollars)")
plt.title("Top 10 Countries by GDP")
plt.tight_layout()
plt.savefig("output/chart3.png")
plt.close()


# Find five results
correlation = latest["gdp"].corr(latest["life"])

low = latest[
    latest["gdp"] <= latest["gdp"].quantile(0.25)
]["life"].mean()

high = latest[
    latest["gdp"] >= latest["gdp"].quantile(0.75)
]["life"].mean()

first_year = int(data["year"].min())

first_life = data[
    data["year"] == first_year
]["life"].median()

last_life = latest["life"].median()

richest = latest.loc[latest["gdp"].idxmax()]


# Save the results in a text file
with open("output/findings.md", "w", encoding="utf-8") as file:
    file.write("# Five Findings\n\n")

    file.write(
        f"1. The link between GDP and life expectancy was "
        f"{correlation:.2f} in {year}.\n\n"
    )

    file.write(
        f"2. Countries with lower GDP had an average life "
        f"expectancy of {low:.1f} years.\n\n"
    )

    file.write(
        f"3. Countries with higher GDP had an average life "
        f"expectancy of {high:.1f} years.\n\n"
    )

    file.write(
        f"4. Median life expectancy changed from "
        f"{first_life:.1f} years in {first_year} to "
        f"{last_life:.1f} years in {year}.\n\n"
    )

    file.write(
        f"5. {richest['country']} had the highest GDP per person "
        f"in {year}: ${richest['gdp']:,.0f}.\n\n"
    )

    file.write("# Limitations\n\n")
    file.write(
        "- Some countries have missing data.\n"
        "- GDP is measured in US dollars and changes with prices.\n"
        "- GDP does not show how money is shared among people.\n"
        "- A link between two things does not prove that one causes the other.\n"
        "- Health and education can also affect life expectancy.\n"
    )

print("Done! Check the output folder.")