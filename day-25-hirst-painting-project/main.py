# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv('weather_data.csv')
# temperature = data['temp']
# monday = data[data['day'] == 'Monday']
# fahrenheit = (monday.temp*9)/5 + 32
# print(fahrenheit)

squirrel = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(squirrel.columns)
squirrel_count = pd.DataFrame(squirrel['Primary Fur Color'].value_counts())
squirrel_count.to_csv('squirrel_count.csv')
print(squirrel_count)



