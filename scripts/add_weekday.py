__author__ = 'Christian'
import csv
from datetime import date
import pandas as pd

header_flag = True

data = []


with open('../data/reduced_v1.1.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if header_flag:
            header = row
            header_flag = False
        else:
            data.append(row)

print(header, len(header))


for i in range(0, len(header)):
    if header[i] == "orderDate":
        index_of_orderDate = i

header.append("weekDay")
header.append("weekEnd")
header.append("month")

for x in range(0,len(data)):
    date_string = data[x][index_of_orderDate].split(" ")[0]
    date_array = date_string.split("/")
    day = int(date_array[1])
    month = int(date_array[0])
    year = int(date_array[2]) + 2000
    date_for_row = date(year, month, day)
    weekday = date_for_row.weekday()
    #Set the weekday for the date (0 = Monday, 6 = Sunday)
    data[x].append(weekday)
    #Set if the date is on a weekend
    if weekday == 5 or weekday == 6:
        data[x].append(1)
    else:
        data[x].append(0)
    #Set month
    data[x].append(date_for_row.month)


print(header, len(header))

header_flag_write = True

pd_data = pd.DataFrame(data, columns = header)


pd_data.to_csv("../output/reduced_v1.2.csv", index = False, header = True)