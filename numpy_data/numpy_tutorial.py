import numpy as np

temp = [1, 2, 3, 4, 5, 6] 
np_temp = np.array(temp)
print(3 * np_temp)
print([3 * x for x in temp])

print(np.array([42, 127], np.int8))


