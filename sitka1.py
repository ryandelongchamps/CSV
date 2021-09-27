import csv

open_file = open("sitka_weather_07-2018_simple.csv","r")

csv_file = csv.reader(open_file,delimiter = ",")

header_row = next(csv_file)

print(type(header_row))


# get index value of a list
for index, column_header in enumerate(header_row):
    print(index, column_header)

# create empty list for highs
highs = []

# for loop to append max temperature to highs
for row in csv_file:
    highs.append(int(row[5]))

print(highs)

# create pyplot object to create chart

import matplotlib.pyplot as plt

#configure chart attributes
plt.title("Daily High Temperatures, July 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)",fontsize = 12)
plt.tick_params(axis="both",which="major",labelsize = 12)

# import data into chart
plt.plot(highs,c="red")

plt.show()