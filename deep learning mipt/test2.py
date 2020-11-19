import numpy as np
import random
import scipy.stats as sps
from copy import copy


def transform(X, a=1):
    X1 = copy(X)
    try:
        if X.shape[1]:
            for string in X:
                for i in range(len(string)):
                    if i % 2 == 0:
                        string[i] = string[i] ** 3
                    else:
                        string[i] = a
                string[::] = string[::-1]
        return np.column_stack((X1, X))
    except IndexError:
        string = X
        for i in range(len(string)):
            if i % 2 == 0:
                string[i] = string[i] ** 3
            else:
                string[i] = a
        string[::] = string[::-1]
        X = string
        return np.array(list(X1) + list(string))



X = np.array([i for i in range(1, 10, 2)])
#print(X.shape[1])
X = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
print(transform(X))
