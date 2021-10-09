# 2. Create an array of size (3, 4) and reshape to (4, 3).

import numpy as np
arr1=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
arr2=np.reshape(arr1,(4,3))
print(arr1)
print(arr2)