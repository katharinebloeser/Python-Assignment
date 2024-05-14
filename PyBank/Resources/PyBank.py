import os

import csv

from datetime import datetime

csvpath=os.path.join("..","MODULE 3 ASSIGNMENT","PyBank", "Resources","budget_data.csv")

date=[]
profitslosses=[]

with open(csvpath,encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")

        next(csvreader)

        for row in csvreader:
            date.append(datetime.strptime(row[0], "%b-%y"))
            profitslosses.append(int(row[1]))

num_months = len(date)

total = sum(profitslosses)
totaldollars = "${:.0f}".format(total)
total_padded = "Total:{:>8}".format(totaldollars)
#StackOverFlow--I used this to help with formatting variables

monthdiffs = []

for i in range(len(profitslosses)-1):
      monthdiff=profitslosses [i+1] - profitslosses[i]
      monthdiffs.append(monthdiff)
#ChatGPT--I used this to figure out why my initial code wasn't working

averagechange = []

averagechange = sum(monthdiffs)/len(monthdiffs)
avgchgdollars = "${:.2f}".format(averagechange)
avgchg_padded = "Average Change: {:>8}".format(avgchgdollars)

greatinc = max(monthdiffs)
greatincdollars = "(${:.0f})".format(greatinc)

greatinc_max = monthdiffs.index(max(monthdiffs))
dategreatinc = date[greatinc_max + 1]
dategreatinc = dategreatinc.strftime("%b-%y")

lowinc = min(monthdiffs)
lowincdollars = "(${:.0f})".format(lowinc)

lowinc_min = monthdiffs.index(min(monthdiffs))
datelowinc = date[lowinc_min]
datelowinc = datelowinc.strftime("%b-%y")


print("Financial Analysis")
print("------------------------------")
print("Total Months: " , num_months)
print(total_padded)
print (avgchg_padded)
print("Greatest Increase in Profits: " + (dategreatinc) + (greatincdollars) )
#why is this the wrong date?
print("Greatest Decrease in Profits: " + (datelowinc) + (lowincdollars) )
#wrong date again


