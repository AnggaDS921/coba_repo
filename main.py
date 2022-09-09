import numpy as np

# menampilkan angka dari 0 sampai 10
A = np.uniform(-.5, .5, size=(4,5))
B = np.uniform(-.5, .5, size=(4,5))


print(np.dot(A, B.T))
print(np.arange(10, 100))
