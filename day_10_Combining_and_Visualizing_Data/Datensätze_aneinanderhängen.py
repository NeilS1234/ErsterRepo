import pandas as pd

januar = pd.DataFrame({
    "Monat": ["Januar", "Januar"],
    "Verkaeufe": [100, 150]
})

februar = pd.DataFrame({
    "Monat": ["Februar", "Februar"],
    "Verkaeufe": [200, 180]
})

gesamt = pd.concat(
    [januar, februar],
    ignore_index=True
)

print(gesamt)