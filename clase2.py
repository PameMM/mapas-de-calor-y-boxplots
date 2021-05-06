#%%

import numpy as np 
import pandas as pd 

#%%
df = pd.read_csv("insurance.csv")
print(df)
# %%
df.tail(3)

# %%
df [['age','bmi']].head(2)
# %%

# %%
df[10:11]

# %%
