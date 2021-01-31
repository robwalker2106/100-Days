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

weather_data = pd.read_csv('weather_data.csv')

print(weather_data['temp'])
