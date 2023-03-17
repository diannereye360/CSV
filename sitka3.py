# 1) changing the file to include all the data for the year of 2018
# 2) change the title to - Daily and low high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the are between high and low

import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv','r')

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
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

print(highs)

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

plt.subplot(2,1,1) # rows, columns, 
plt.plot(dates,highs,c='red')
plt.title ('highs')

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title('lows')

plt.suptitle('highs and lows of sitka, alaska')
plt.show()
