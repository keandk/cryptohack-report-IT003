import numpy as np

mat = np.array([[6, 2, -3],[5, 1, 4], [2, 7, 1]])

det = np.linalg.det(mat)
print(round(abs(det)))
