import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    result = 1 / (1 + np.exp(-z))
    return result

y1 = np.sum(x*c1)
y2 = np.sum(x*c2)
y3 = np.sum(x*c3)
print(sigmoid(y1))
print(sigmoid(y2))
print(sigmoid(y3))
# calculate the output of the sigmoid for x with all three coefficients