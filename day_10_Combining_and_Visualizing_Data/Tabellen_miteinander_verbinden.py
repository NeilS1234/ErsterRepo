import pandas as pd

namen = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Anna", "Ben"]
})

noten = pd.DataFrame({
    "ID": [1, 2],
    "Note": [2, 1]
})

ergebnis = pd.merge(namen, noten, on="ID")
print(ergebnis)