import csv
import pandas as pd

# data = []

# with open('weather_data.csv') as file:
#     lines = csv.reader(file)
#     temperatures = []
#     for line in lines:
#         data.append(line)
#         if line[1] != 'temp':
#             temperatures.append(int(line[1]))
#     print(temperatures)
#
# weather_data = pd.read_csv('weather_data.csv')
#
# print(weather_data)
#
# weather_data.temp = weather_data.apply(lambda x: (int(x.temp) * 9/5) + 32, axis=1)
#
# print(weather_data)

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# for color in new_colors:
#     count.append(squirrel_data[squirrel_data['Primary Fur Color'] == color].count())

gray_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

new_data = {'Primary Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [gray_count, cinnamon_count, black_count]}

new_pd = pd.DataFrame(new_data)

new_pd.to_csv('squirrel_count.csv')

