import pandas as pd
import numpy as np

A = np.random.randn(10, 2)
B = np.random.randn(10, 2)


print(np.dot(A, B.T))
