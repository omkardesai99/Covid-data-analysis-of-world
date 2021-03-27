import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

files = os.listdir(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets")
files
def read_data(path,filename):
    a=pd.read_csv(path + '/' + filename)
    return a

path=r'C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets'
country_wise_data=read_data(path,files[0])
province_data=read_data(path,files[1])
day_wise_data=read_data(path,files[2])
group_data=read_data(path,files[3])
usa_data=read_data(path,files[4])
world_data=read_data(path,files[5])

#--------------------------------------------------  OR  ----------------------------------------------------------------------

province_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\covid_19_clean_complete.csv")

world_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\worldometer_data.csv")

country_wise_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\country_wise_latest.csv")

day_wise_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\day_wise.csv")

usa_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\usa_country_wise.csv")

group_data=pd.read_csv(r"C:\Users\omkar desai\OneDrive\Desktop\data analysis\covid datasets\full_grouped.csv")

province_data.shape

world_data.columns

import plotly.express as px
# OR 
import plotly.graph_objs as go
import plotly.offline as ply

#TASK1:-
#PART1:
columns=[ 'TotalCases','TotalDeaths','TotalRecovered','ActiveCases']
for i in columns:
    fig=px.treemap(world_data.iloc[0:20],values=i,path=['Country/Region'],title='tree map of covid data of world of countries w.r.t to their  {}'.format(i))
    fig.show()

#*************************************************************************************************************************************
country=world_data['Country/Region'].iloc[0:20]   
len(country)
count=world_data['TotalCases'].iloc[0:20] 
plt.pie(count,labels=country,autopct='%0.0f%%',explode=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#*************************************************************************************************************************************
country=world_data['Country/Region']  
len(country)
count=world_data['TotalCases'] 
plt.pie(count,labels=country,autopct='%0.0f%%',explode=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#*************************************************************************************************************************************

country=world_data['Country/Region'].iloc[0:20]  
count=world_data['TotalCases'].iloc[0:20] 
plt.stem(country, count, use_line_collection = True) 


'''
a=['a','b','c']
p=[10,20,30]
l=[5,10,15]
m=np.arange(len(a))

plt.bar(m+0.2,p,width=0.4)
plt.bar(m-0.2,l,width=0.4)
plt.xticks(m,a)
plt.ylim(0,40)
'''

day_wise_data.columns
plt.plot(day_wise_data['Date'],day_wise_data['Confirmed'],label="Confirmed cases")
plt.plot(day_wise_data['Date'],day_wise_data['Deaths'],label="Deaths")
plt.plot(day_wise_data['Date'],day_wise_data['Recovered'],label="Recovered cases")
plt.plot(day_wise_data['Date'],day_wise_data['Active'],label="Active cases")

plt.title('covid cases data of the world')
plt.ylim(0,20000000)
plt.ylabel('number of cases in million')
plt.xlabel('Days')
plt.grid()
plt.legend(loc='best')
#-----------------------------------------------------------------OR------------------------------------------------------------------
#PART2:
day_wise_data.shape
px.line(day_wise_data,x='Date',y=['Confirmed', 'Deaths', 'Recovered', 'Active'],title='covid cases wrt world' ,template='plotly_dark')

#OR
box=go.Line(day_wise_data,x=['Date'],y=['Confirmed', 'Deaths', 'Recovered', 'Active'],title='covid cases wrt world' ,template='plotly_dark')

data=[box]
ply.plot(data,filename='covid cases wrt world')
#------------------------------------------------------------------------------------------------------------------------------------

#TASK2:-
#PART1:
world_data.columns
pop_test_ratio=(world_data['Population']/world_data['TotalTests']).iloc[0:20]
#OR
pop_test_ratio=(world_data['Population']/world_data['TotalTests'])
pop_test_ratio[0:20]

plt.bar(world_data['Country/Region'],pop_test_ratio[0:20],width=0.4)

#OR

fig=px.bar(world_data.iloc[0:20],x=['Country/Region'],y=pop_test_ratio[0:20],title='bar of covid data of world of countries')
fig.show()
#------------------------------------------------------------------------------------------------------------------------------------
#PART2:
#we cannot us list[] in both x and y at the same time
fig=px.bar(world_data.iloc[0:20],x='Country/Region',y=['TotalCases','TotalDeaths', 'TotalRecovered','ActiveCases', 'Serious,Critical'], title='bar of covid data of world of countries')
fig.show()
#------------------------------------------------------------------------------------------------------------------------------------

#TASK3:-
#top 20 countries with worst TotalCases
fig=px.bar(world_data.iloc[0:20],x='TotalCases',y='Country/Region',color='TotalCases',title='totalcases')
fig.update_layout(template='plotly_dark',title_text='top 20 countries of total cases')
fig.show()

#top 20 countries with worst TotalDeaths
fig=px.bar(world_data.sort_values(by='TotalDeaths',ascending=False)[0:20],x='TotalDeaths',y='Country/Region', color='TotalDeaths', title='TotalDeaths')
fig.update_layout(template='plotly_dark',title_text='top 20 countries of total Deaths cases')
fig.show()

#top 20 countries with worst ActiveCases
fig=px.bar(world_data.sort_values(by='ActiveCases',ascending=False)[0:20],x='ActiveCases',y='Country/Region', color='ActiveCases', title='ActiveCases')
fig.update_layout(template='plotly_dark',title_text='top 20 countries of ActiveCases')
fig.show()

#top 20 countries with worst Serious,Critical
fig=px.bar(world_data.sort_values(by='Serious,Critical',ascending=False)[0:20],x='Serious,Critical',y='Country/Region', color='Serious,Critical',title='Serious,Critical')
fig.update_layout(template='plotly_dark',title_text='top 20 countries of ActiveCases')
fig.show()



columns=['TotalCases','TotalDeaths', 'TotalRecovered','ActiveCases']
for i in columns:
    fig=px.bar(world_data.sort_values(by=i,ascending=False)[0:20],x=i,y='Country/Region',color=i,title=i)
    fig.update_layout(template='plotly_dark',title_text='top 20 countries of {}'.format(i))
    fig.show()

#TASK4:-
#PART1:
labels=world_data.iloc[0:15]['Country/Region'].values
cases=['TotalCases','TotalDeaths', 'TotalRecovered','ActiveCases', 'Serious,Critical']
for i in cases:
    fig=px.pie(world_data.iloc[0:15],values=i,names=labels,hole=0.3,title='top 15 countries of {}'.format(i))
    fig.show()

#PART2:
death_to_confirmed_ratio=(world_data['TotalDeaths']/world_data['TotalCases']).iloc[0:20]
fig=px.bar(world_data.iloc[0:20],x=['Country/Region'],y=death_to_confirmed_ratio,color=death_to_confirmed_ratio,title='bar of covid data of world of countries of death_to_confirmed_ratio')
fig.show()

#PART3:
death_to_Recovered_ratio=(world_data['TotalDeaths']/world_data['TotalRecovered']).iloc[0:20]
fig=px.bar(world_data.iloc[0:20],x=['Country/Region'],y=death_to_Recovered_ratio,title='bar of covid data of world of countries of death_to_Recovered_ratio')
fig.show()

#PART4:
Tests_to_confirmed_ratio=(world_data['TotalTests']/world_data['TotalCases']).iloc[0:20]
fig=px.bar(world_data.iloc[0:20],x=['Country/Region'],y=Tests_to_confirmed_ratio,title='bar of covid data of world of countries of Tests_to_confirmed_ratio')
fig.show()

#PART5:
Serious_to_Deaths_ratio=(world_data['Serious,Critical']/world_data['TotalDeaths']).iloc[0:20]
fig=px.bar(world_data.iloc[0:20],x=['Country/Region'],y=Serious_to_Deaths_ratio,title='bar of covid data of world of countries of Serious_to_Deaths_ratio')
fig.show()
