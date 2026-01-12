import numpy as np

def euclidean(input1, input2):
    return np.sqrt(np.sum((np.array(input1) - np.array(input2))**2))

x = [1.5, 2.0, 3.5]
y = [4.0, 1.0, 2.5]
print(euclidean(x, y))