# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:30:15 2023

@author: Lenovo
"""

#Importing libraries
import pandas as pd
import numpy as np
import statistics

#Importing data
del_data = pd.read_csv('onlinedeliverydata.csv')

#Copy data for feature engg
df = del_data.copy()


#Feature engineering

#Creating dictionaries for updating files
importance_map = {'Unimportant':0,
                  'Slightly Important':1,
                  'Moderately Important':2,
                  'Important':3,
                  'Very Important':4
                  }

yes_no_map = {'Yes':1,
              'No':-1,
              'Maybe':0    
              }

agree_map = {'Strongly disagree':-2,
             'Disagree':-1,
             'Neutral':0,
             'Agree':1,
             'Strongly agree':2,
             'Strongly Agree':2
             }

education_map={'Uneducated':0,
               'School':1,
               'Graduate':2,
               'Post Graduate':3,
               'Ph.D':4
              }

waiting_time_map = {'15 minutes':1,
                   '30 minutes':2,
                   '45 minutes':3,
                   '60 minutes':4,
                   'More than 60 minutes':5}

#Updating columns
col_upd = ['Less Delivery time','High Quality of package', 'Number of calls', 'Politeness','Freshness ', 'Temperature', 'Good Taste ', 'Good Quantity']
for i in range(len(col_upd)):
    df[col_upd[i]] = df[col_upd[i]].map(importance_map)
    
col_upd_1 = ['Influence of rating','Influence of time', 'Output']
for i in range(len(col_upd_1)):
    df[col_upd_1[i]] = df[col_upd_1[i]].map(yes_no_map)
    
col_upd_2 = ['Ease and convenient','Time saving','More restaurant choices','Easy Payment option','More Offers and Discount',
             'Good Food quality','Good Tracking system','Self Cooking','Health Concern','Late Delivery','Poor Hygiene',
             'Bad past experience','Unavailability','Unaffordable','Long delivery time','Delay of delivery person getting assigned',
             'Delay of delivery person picking up food','Wrong order delivered','Missing item','Order placed by mistake',
             'Residence in busy location','Google Maps Accuracy','Good Road Condition','Low quantity low time','Delivery person ability']

for i in range(len(col_upd_2)):
    df[col_upd_2[i]] = df[col_upd_2[i]].map(agree_map)
    
#Income column
old_income = ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000']
new_income = ['0', '<10k', '10k-25k', '25k-50k', '>50k']
for i in range(len(old_income)):
    df.loc[df['Monthly Income']==old_income[i], 'Monthly Income'] = new_income[i]
    
#Converting gender column to IsMale
df.rename(columns = {'Gender':'IsMale'}, inplace = True)
df['IsMale'] = np.where(df["IsMale"] == "Male", 1, 0)

#Educational Qualifications column
df['Educational Qualifications'] = df['Educational Qualifications'].map(education_map)

#Marital status, replacing unknown status with mode value
df.loc[df['Marital Status'] == 'Prefer not to say', 'Marital Status'] = statistics.mode(df['Marital Status'])
df.rename(columns = {'Marital Status':'IsMarried'}, inplace = True)
df['IsMarried'] = np.where(df["IsMarried"] == "Married", 1, 0)

df['Maximum wait time'] = df['Maximum wait time'].map(waiting_time_map)