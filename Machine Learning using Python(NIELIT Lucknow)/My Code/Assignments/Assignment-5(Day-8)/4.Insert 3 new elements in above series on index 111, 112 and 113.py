# Insert 3 new elements in above series on index 111, 112 and 113.

import pandas as pd
i=list(range(101,111))
data=['A','B','C','D','E','F','G','H','I','J']
s=pd.Series(data,index=i)
print(s)
s1=pd.Series(('L','M','N'),index=(111,112,113))
s2=s.append(s1)
print(s2)