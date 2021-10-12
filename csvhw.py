import csv
import matplotlib.pyplot as plt
from datetime import datetime

dvdate = []
dvhigh = []
dvlow = []
dvname = []
sitkadate = []
sitkahigh = []
sitkalow = []
sitkaname = []

infilesitka = open("sitka_weather_2018_simple.csv", "r")
csvsitka = csv.reader(infilesitka, delimiter=",")
sitkaheaderrow = next(csvsitka)
sitkahighindex = sitkaheaderrow.index("TMAX")
sitkalowindec = sitkaheaderrow.index("TMIN")
sitkadateindex = sitkaheaderrow.index("DATE")
sitkanameindex = sitkaheaderrow.index("NAME")

infiledv = open("death_valley_2018_simple.csv", "r")
csvdv = csv.reader(infiledv, delimiter=",")
dvheaderrow = next(csvdv)
dvhighindex = dvheaderrow.index("TMAX")
dvlowindex = dvheaderrow.index("TMIN")
dvdateindex = dvheaderrow.index("DATE")
dvnameindex = dvheaderrow.index("NAME") 

for row in csvsitka:
    try:
        shigh = int(row[sitkahighindex])
        slow = int(row[sitkalowindec])
        sdate = datetime.strptime(row[sitkadateindex], "%Y-%m-%d")
        sname = str(row[sitkanameindex])
    except ValueError:
        print(f"Missing data for {sdate}")
    else:
        sitkahigh.append(shigh)
        sitkalow.append(slow)
        sitkadate.append(sdate)
        sitkaname.append(sname)

for row in csvdv:
    try:
        dhigh = int(row[dvhighindex])
        dlow = int(row[dvlowindex])
        ddate = datetime.strptime(row[dvdateindex], "%Y-%m-%d")                            
        dname = str(row[dvnameindex])
    except ValueError:
        print(f"Missing data for {ddate}")
    else:
        dvhigh.append(dhigh)
        dvlow.append(dlow)
        dvdate.append(ddate)
        dvname.append(dname)

print(dvname[1])
print(sitkaname[1])
print(dvhighindex)
print(dvlowindex)
print(sitkahighindex)
print(sitkalowindec)

plt.subplot(2, 1, 1)
plt.plot(sitkadate, sitkahigh, c = "red")
plt.plot(sitkadate, sitkalow, c = "blue")
plt.fill_between(sitkadate, sitkahigh, sitkalow, facecolor = "blue", alpha = 0.1)
plt.title(sitkaname[1])

plt.subplot(2, 1, 2)
plt.plot(dvdate, dvhigh, c = "red")
plt.plot(dvdate, dvlow, c = "blue")
plt.fill_between(dvdate, dvhigh, dvlow, facecolor = "blue", alpha = 0.1)
plt.title(dvname[1])

plt.suptitle("Temperature comparison between " + str(sitkaname[1]) + " and " + str(dvname[1]))
plt.show()