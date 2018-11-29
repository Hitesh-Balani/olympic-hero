# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar')
plt.xlabel('United States')
plt.ylabel('Medals Tally') 

#plt.xticks(rotation=45)


# --------------
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] ,'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
a = data['Better_Event'].value_counts().index.tolist()
better_event = a[0]
print(better_event)


# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(top_countries,Total_Summer,Total_Winter,Total_Medals):
    country_list_summer=list()
    country_list_winter=list()
    country_list_medals=list()
    country_list_summer = list((top_countries.nlargest(10,Total_Summer)['Country_Name']))
    country_list_winter = list((top_countries.nlargest(10,Total_Winter)['Country_Name']))
    country_list_medals = list((top_countries.nlargest(10,Total_Medals)['Country_Name']))    
    return country_list_summer,country_list_winter,country_list_medals

topten = list(top_ten(top_countries,'Total_Summer','Total_Winter','Total_Medals'))

top_10_summer=topten[0]
print(top_10_summer)

top_10_winter=topten[1]
print(top_10_winter)

top_10=topten[2]
print(top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(20,10))
summer_df[['Country_Name','Total_Summer']].plot(kind='bar',ax=ax_1)
winter_df[['Country_Name','Total_Winter']].plot(kind='bar',ax=ax_2)
top_df[['Country_Name','Total_Medals']].plot(kind='bar',ax=ax_3)


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points']=( (data_1['Gold_Total']*3) +  (data_1['Silver_Total']*2) + data_1['Bronze_Total'] )

most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']



# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_max_ratio)
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']


top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']



