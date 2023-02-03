import numpy as np
x = np.array([1,2,3,99,99,3,2,1])
np.split(x, [3,5])



m = np.arange(12,20).reshape(2,4)
sag, sol = np.hsplit(m, [3])
print(sag)
print(sol)

