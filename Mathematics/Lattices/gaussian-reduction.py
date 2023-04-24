from Crypto.Util.number import inverse
import math
import numpy as np

def gaussian_reduction(v1, v2):
    while True:
        #Swap 2 vector if size V2 < size V1
        #Require sizeV1 < sizeV2
        if np.dot(v2, v2) < np.dot(v1, v1):
            v = v2
            v2 = v1
            v1 = v
        m = np.dot(v1,v2)//np.dot(v1,v1) #an integer
        if m == 0:
            return v1, v2
        v2 = v2 - m * v1

v1 = np.array([846835985, 9834798552])
v2 = np.array([87502093, 123094980])

v1, v2 = gaussian_reduction(v1, v2)

print(np.dot(v1, v2))
