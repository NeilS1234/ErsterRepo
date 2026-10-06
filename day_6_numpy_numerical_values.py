import numpy as np

# Numerical values
values = np.array([10, 20, 30, 40, 50])

# Calculations
total = np.sum(values)
mean = np.mean(values)
median = np.median(values)
minimum = np.min(values)
maximum = np.max(values)
standard_deviation = np.std(values)

# Percentage difference from the mean
percentage_difference = ((values - mean) / mean) * 100

# Results
print("Values:", values)
print("Total:", total)
print("Mean:", mean)
print("Median:", median)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard deviation:", standard_deviation)
print("Percentage difference from the mean:", percentage_difference)

