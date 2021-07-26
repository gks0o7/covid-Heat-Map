#it is a covid-19 live map using live data from website worldometers



from bs4 import BeautifulSoup

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import requests

import geopandas as gpd



live_data= requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/').content

data=pd.read_html(live_data)

df=data[0]
id=list(range(1,221))
df['s. no']=id
df.set_index('s. no' , inplace = True)

print(df.head())






#manipulating data to plot a graph 



#Selecting top countries with coronavirus cases 

data=df.iloc[0:15]

#filling null value with 0.

data=data.fillna(0)

print(data)







#plotting countries with number of total cases

plt.figure(figsize=(20,8))

plt.barh(data["Country"],data["Cases"],  color = 'blue')

plt.title("Countries with most number of covid-19 cases ",fontsize = 30)

plt.xlabel("cases", fontsize=30)

plt.ylabel("Countries", fontsize=30)

plt.xticks(fontsize = 20)

plt.yticks(fontsize = 20)

plt.show()





#Reading shape file of world countries

data_map = gpd.read_file('World_Countries__Generalized_.shp')

#Changing the name of column that we want to merge with data

data_map.rename(columns = {'COUNTRYAFF':'Country'}, inplace = True)

#plotting sample of world map

data_map.plot()






data_map['Country'].replace('Congo DRC',

                              'DR Congo', inplace = True)
data_map['Country'].replace('Russian Federation',

                              'Russia', inplace = True)


#merging both datasets on column country

merged = pd.merge(data_map,df, on = "Country")
pd.set_option('display.max_rows',232)
merged






#plotting coronavirus cases on world map 

fig, ax = plt.subplots(1, figsize=(30, 10))

ax.axis('off')

ax.set_title('Coronavirus Cases in the World', fontsize=25)

merged.plot(column = 'Cases', cmap='coolwarm', 

                 linewidth=0.8, ax=ax, edgecolor='0.8', 

                 legend = True)

plt.show()
