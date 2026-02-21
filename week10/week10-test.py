# import numpy as np
# import scipy as sp
# print("NumPy version:", np.__version__)
# print("SciPy version:", sp.__version__)

# import numpy as np

# a = np.array([1, 2, 3])
# print (a)

# b= np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# print(b)
# print(b.ndim)  # number of dimensions
# print(b.shape)  # shape of the array

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)

# print(a[1,5])


import numpy as np
import pandas as pd
import time

#Creating a large DataFrame
data = pd.DataFrame(np.random.rand(100000, 4), columns=['A', 'B', 'C', 'D'])

# # Timing Pandas operations
# start_time = time.time()
# result_pandas = data[(data['A'] > 0.5) & (data['B'] < 0.5)].mean()
# end_time = time.time()
# print("Pandas Conditional Mean:\n", result_pandas)
# print("Pandas Operation Time: {:.5f} seconds".format(end_time - start_time))

# # Timing equivalent NumPy operations
# numpy_data = data.to_numpy()
# start_time = time.time()
# result_numpy = np.mean(numpy_data[(numpy_data[:, 0] > 0.5) & (numpy_data[:, 1] < 0.5)], axis=0)
# end_time = time.time()
# print("NumPy Conditional Mean:\n", result_numpy)
# print("NumPy Operation Time: {:.5f} seconds".format(end_time - start_time))

import matplotlib.pyplot as plt

# Plotting with NumPy arrays
plt.scatter(data['A'], data['B'], alpha=0.5)
plt.title("Custom Scatter Plot")
plt.xlabel("A")
plt.ylabel("B")
plt.show()