import csv

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for row in csvfile:
    highs.append(row[5])

print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red") #creates line graph
plt.title('Daily Temp July 2018', fontsize=16)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()