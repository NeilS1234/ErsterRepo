import pandas as pd

namen = pd.DataFrame(
    {"Name": ["Anna", "Ben"]},
    index=[1, 2]
)

noten = pd.DataFrame(
    {"Note": [2, 1]},
    index=[1, 2]
)

ergebnis = namen.join(noten)
print(ergebnis)