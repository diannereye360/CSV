# 1) handle error checking using try and except
# 2) change file to use death valley data

import csv
from datetime import datetime

infile = open('death_valley_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = [] #y-axis
lows = [] #y-axis
dates = [] #x-axis

#somedate = datetime.strptime('2018-07-01','%Y-%m-%d')

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        #highs.append(int(row[4]))
        #lows.append(int(row[5]))
        thedate = datetime.strptime(row[2],'%Y-%m-%d')
        #dates.append(thedate)
    except ValueError:
        print(f'Missing data for {thedate}')

    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)

#print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates,highs,c='red', alpha=0.5) #alpha -> transparency
plt.plot(dates,lows,c='blue', alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='purple', alpha=0.1)

#plt.plot(highs, c="red") #creates line graph
plt.title('Daily Highs and Low Temperatures - 2018', fontsize=16)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

fig.autofmt_xdate()
plt.show()

