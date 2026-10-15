import matplotlib.pyplot as plt

monate = ["Jan", "Feb", "Mär", "Apr"]
verkaeufe = [100, 150, 130, 220]

plt.bar(monate, verkaeufe)
plt.title("Verkäufe pro Monat")
plt.xlabel("Monat")
plt.ylabel("Verkäufe")
plt.show() 