import numpy as np
import pandas as pd
index = [0,1,2,3,4,5]
s = pd.Series([1,2,3,4,5,6],index= index)
t = pd.Series([2,4,6,8,10,12],index= index)
df = pd.DataFrame(s,columns = ["MUL1"])
df["MUL2"] =t

print df
