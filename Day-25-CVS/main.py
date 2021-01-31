import csv

data = []

with open('weather_data.csv') as file:
    lines = csv.reader(file)
    for line in lines:
        data.append(line)

print(data)
