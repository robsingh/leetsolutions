'''
DataFrame : Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this dataframe.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

'''

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # ensure the recordDate column is in datetime format
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    #sort the df by recordDate
    weather = weather.sort_values(by="recordDate")

    #calculate the difference in temperatures
    weather['temp_diff'] = weather['temperature'].diff()
    
    #calculate the difference in dates
    weather['date_diff'] = weather['recordDate'].diff().dt.days

    # filter rows with rising temperature and consecutive dates
    result = weather[(weather['temp_diff'] > 0) & (weather['date_diff'] == 1)]

    return result[['id']]
    

data = {
    'id': [1,2,3,4],
    'recordDate':['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature':[10,20,30,40]
}

weather = pd.DataFrame(data)

result = rising_temperature(weather)
print(result)