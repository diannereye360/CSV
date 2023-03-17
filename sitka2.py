# using the datetime module
# adding the dates to the xaxis for the month of July 2018
import csv
from datetime import datetime

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = [] #y-axis
dates = [] #x-axis

#somedate = datetime.strptime('2018-07-01','%Y-%m-%d')

for row in csvfile:
    highs.append(int(row[5]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates,highs,c='red')

#plt.plot(highs, c="red") #creates line graph
plt.title('Daily Temp July 2018', fontsize=16)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

fig.autofmt_xdate()
plt.show()