import numpy as np

v0 = np.array([4,1,3,-1])
v1 = np.array([2,1,-3,4])
v2 = np.array([1,0,-2,7])
v3 = np.array([6,2,9,-5])
v = [v0, v1, v2, v3]
u = v
u[0] = v[0]

for i in range (1, 4):
    t = [0,0,0,0]
    for j in range (0, i):
        t[j] = np.dot(v[i], u[j]) / np.dot(u[j], u[j])
    for j in range (0, i):
        u[i] = v[i] - t[j] * u[j]


print(round(u[3][1], 5))
