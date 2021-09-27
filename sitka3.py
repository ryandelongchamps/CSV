import csv

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter = ",")

header_row = next(csv_file)

print(type(header_row))


# get index value of a list
for index, column_header in enumerate(header_row):
    print(index, column_header)

#testing to convert date from string
#2018-07-01

from datetime import datetime
mydate = datetime.strptime('2018-07-01','%Y-%m-%d')
print(mydate)

#create empty list for date
dates = []

# create empty list for highs
highs = []
lows = []

# for loop to append max temperature to highs and dates
for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(row[6]))
'''
print(highs)
print(dates)
print(lows)
'''

# create pyplot object to create chart

import matplotlib.pyplot as plt

fig = plt.figure()

#configure chart attributes
plt.title("Daily Temperatures, 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)",fontsize = 12)
plt.tick_params(axis="both",which="major",labelsize = 12)

# import data into chart
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c='blue',alpha = 0.5)

#shade in between area
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#create figure object to format y axis
fig.autofmt_xdate()


#show graph
plt.show()

