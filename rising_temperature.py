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
    #ensure df is sorted by 'recordDate'
    weather = weather.sort_values(by='recordDate')

    # shift the temperature column to get the previous day's temperature
    weather['prev_temperature'] = weather['temperature'].shift(1)

    #find all the rows where current day's temperature is greater than the previous day
    result = weather[weather['temperature'] > weather['prev_temperature']]

    return result['id']

data = {
    'id': [1,2,3,4],
    'recordDate':['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature':[10,20,30,40]
}

weather = pd.DataFrame(data)

result = rising_temperature(weather)
print(result)