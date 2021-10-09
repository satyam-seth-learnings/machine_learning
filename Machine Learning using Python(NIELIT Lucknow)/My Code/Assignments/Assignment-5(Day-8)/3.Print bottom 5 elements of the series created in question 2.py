# Print bottom 5 elements of the series created in question 2.

import pandas as pd
i=list(range(101,111))
data=['A','B','C','D','E','F','G','H','I','J']
s=pd.Series(data,index=i)
print(s.tail())