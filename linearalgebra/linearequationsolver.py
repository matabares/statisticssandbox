#solve 7x-5y = 3

import numpy as np
import pprint
coef = np.array([[2,1],[1,2]])
depvar = np.array([100,100])

result = np.linalg.solve(coef, depvar)
print(result)

