#%%
# Se importan las librerías necesarias
import pandas as pd
import seaborn as sns
#%%
# Se lee el archivo CSV
df = pd.read_csv('ulabox_orders_with_categories_partials_2017.csv')
sns.set_theme(style="white")
#%%
# Variables de customer
sns.displot(x="customer", data=df)

#%%
df.info()
# %%
# Variable total_items
sns.boxplot(x="weekday", y="total_items", data=df, palette='rainbow')
# %%
# Variable total_items
sns.displot(x="total_items", data=df)
# %%
# Variable discount%
sns.displot(x="discount%", data=df)

# %%
#Correlación de weekday y discount 

df[['weekday','hour','discount%']].corr()
# %%
#Mapa de calor 
sns.heatmap(df[['weekday','hour','discount%']].corr(), annot=True)
# %%
df.corr()

# %%
sns.heatmap(df.corr(), annot=True)
# %%
#hour
sns.displot(x="hour", data=df)
# %%
#Food%
sns.boxplot(x="weekday", y="Food%", data=df, palette='rainbow')
# %%
#Fresh%
sns.displot(x="Fresh%", data=df)
# %%
#Fresh%
sns.boxplot(x="weekday", y="Fresh%", data=df, palette='rainbow')
# %%
#Drinks%
sns.displot(x="Drinks%", data=df)
# %%
#Drinks%
sns.boxplot(x="weekday", y="Drinks%", data=df, palette='rainbow')
# %%
#Home%
sns.displot(x="Home%", data=df)
# %%
#Beauty%
sns.displot(x="Beauty%", data=df)

# %%
#Health%
sns.displot(x="Health%", data=df)

# %%
#Baby%
sns.displot(x="Baby%", data=df)
# %%
#Pets%
sns.displot(x="Pets%", data=df)
# %%
sns.heatmap(df[['weekday','Food%','Fresh%','Drinks%', 'Home%', 'Beauty%', 'Health%', 'Baby%','Pets%']].corr(), annot=True)
# %%
df[['weekday','Food%','Fresh%','Drinks%', 'Home%', 'Beauty%', 'Health%', 'Baby%','Pets%']].corr()

# %%
