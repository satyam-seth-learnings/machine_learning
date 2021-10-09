# Delete the elements at index- 103, 104,107,111 in above list.

import pandas as pd
i=list(range(101,111))
data=['A','B','C','D','E','F','G','H','I','J']
s=pd.Series(data,index=i)
s1=pd.Series(('L','M','N'),index=(111,112,113))
s2=s.append(s1)
print(s2)
s2.drop(index=[103,104,107,111],inplace=True)
print(s2)