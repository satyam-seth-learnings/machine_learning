# Create a pandas series of 10 elements and specify their index as 101 to 110

import pandas as pd
i=list(range(101,111))
data=['A','B','C','D','E','F','G','H','I','J']
s=pd.Series(data,index=i)
print(s)