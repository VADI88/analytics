from collections import Counter
import numpy as np

def solution(A):
    print(A)
    keys,values = np.unique(A, return_counts=True)
    for i, val in enumerate(values):
        if val %2 !=0:
            return(keys[i])
        else:
            pass

A = [9,9,3,3,9,9,7]
print(solution(A))