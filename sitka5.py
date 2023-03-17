import csv
from datetime import datetime

infile_dv = open('death_valley_2018_simple.csv','r')
infile_s = open('sitka_weather_2018_simple.csv','r')

csvfile_dv = csv.reader(infile_dv)
csvfile_s = csv.reader(infile_s)

header_row_dv = next(csvfile_dv)
header_row_s = next(csvfile_s)

highs_dv = [] 
lows_dv = [] 
dates_dv = [] 
station_dv = []

highs_s = []
lows_s = []
dates_s = []
station_s = []

for row in csvfile_dv:
    try:
        high = int(row[header_row_dv.index('TMAX')])
        low = int(row[header_row_dv.index('TMIN')])
        thedate = datetime.strptime(row[header_row_dv.index('DATE')],'%Y-%m-%d')
        name = (row[header_row_dv.index('NAME')])
    except ValueError:
        print(f'Missing data for {thedate}')
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(thedate)
        station_dv.append(name)

for row in csvfile_s:
    try:
        high = int(row[header_row_s.index('TMAX')])
        low = int(row[header_row_s.index('TMIN')])
        thedate = datetime.strptime(row[header_row_s.index('DATE')],'%Y-%m-%d')
        name = row[header_row_dv.index('NAME')]
    except ValueError:
        print(f'Missing data for {thedate}')
    else:
        highs_s.append(high)
        lows_s.append(low)
        dates_s.append(thedate)
        station_s.append(name)

import matplotlib.pyplot as plt
fig = plt.figure()

plt.subplot(2,1,2)
plt.plot(dates_dv,highs_dv,c='red', alpha=0.5) #alpha -> transparency
plt.plot(dates_dv,lows_dv,c='blue', alpha=0.5)
plt.fill_between(dates_dv,highs_dv,lows_dv,facecolor='purple', alpha=0.1)
plt.title(station_dv[0], fontsize=16)

plt.subplot(2,1,1)
plt.plot(dates_s,highs_s,c='red', alpha=0.5) #alpha -> transparency
plt.plot(dates_s,lows_s,c='blue', alpha=0.5)
plt.fill_between(dates_s,highs_s,lows_s,facecolor='purple', alpha=0.1)
plt.title(station_s[0], fontsize=16)

plt.suptitle('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US')
fig.autofmt_xdate()
plt.show()
