##  objective: to fetch covid19 data from the live data source and perform simple analytics
## 
##  note: this program fetch updated data from the github


import pandas as pd 
import numpy as np 
#import seaborn as sns 
import plotly.express as px
import matplotlib.pyplot as plt

dataset_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv( dataset_url )
print(df.head())
print(df.tail())
print(df.shape)

df = df[df.Confirmed > 0]
print(df.head())
print(df.tail())

df[df=='Pakistan']
print(df.head())


fig = px.choropleth(df, locations = 'Country', locationmode= 'country names', color='Deaths' ,animation_frame='Date')
fig.update_layout(title_text = 'Global spread of Convid-19')
fig.show()


df_china = df[df.Country == 'China']
print(df_china.head())

df_china = df_china['Date', 'Confirmed']
df_china.head()

df_china['Infection Rate'] = df_china['Confirmed'].diff()
df_china.head()

px.line(df_china, x = 'Date', y = ['Confirmed', 'Infection Rate'])

df_china['Infection Rate'].max()
df.head()

countries = list(df['Country'].unique())
max_infection_rates = []
for c in countries:
    MIR = df[df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)
print(max_infection_rates)

df_MIR = pd.DataFrame()
df_MIR['Country'] = countries
df_MIR['Max Infection Rate'] = max_infection_rates
df_MIR.head()

px.bar(df_MIR, x='Country', y = 'Max Infection Rate', color = 'Country', title = 'Global infection rate')


px.bar(df_MIR, x='Country', y = 'Max Infection Rate', color = 'Country', title = 'Global infection rate', log_y=True)




