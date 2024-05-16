import os

import csv

from datetime import datetime

#Locate the CSV file
csvpath=os.path.join("..","MODULE 3 ASSIGNMENT","PyBank", "Resources","budget_data.csv")
#Create the columns
date=[]
profitslosses=[]
#Import the CSV file, skip the first row
with open(csvpath,encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=",")

        next(csvreader)
#For each row in the file, row 1 is a date and row two is an integer
        for row in csvreader:
            date.append(datetime.strptime(row[0], "%b-%y"))
            profitslosses.append(int(row[1]))
#Create a variable for the number of months in the data, which is the number of rows (without the header row)
num_months = len(date)
#Create a variable for the total of the profits and losses, adding each row together, then format that in dollars with zero decimal points, then put this in the 'Total:'
total = sum(profitslosses)
totaldollars = "${:.0f}".format(total)
total_padded = "Total:{:>8}".format(totaldollars)
#StackOverFlow--I used this to help with formatting variables

#Create a variable for the monthly differences
monthdiffs = []
#Create a loop where for each row, it takes the first row and subtracts the previous row and adds it to the monthdiffs variable
for i in range(len(profitslosses)-1):
      monthdiff=profitslosses [i+1] - profitslosses[i]
      monthdiffs.append(monthdiff)
#ChatGPT--I used this to figure out why my initial code wasn't working

#Create a variable for average change
averagechange = []
#Calculate the average change, then format it in dollars with two decimal points, then add the 'Average Change:'
averagechange = sum(monthdiffs)/len(monthdiffs)
avgchgdollars = "${:.2f}".format(averagechange)
avgchg_padded = "Average Change: {:>8}".format(avgchgdollars)

#Identify the greatest increase and then format that amount
greatinc = max(monthdiffs)
greatincdollars = "(${:.0f})".format(greatinc)
#Identify the maximum value of the greatest increase amount, then index that value and give the date
greatinc_max = monthdiffs.index(max(monthdiffs))
dategreatinc = date[greatinc_max + 1]
dategreatinc = dategreatinc.strftime("%b-%y")
#Identify the lowest decrease and then format that amount
lowinc = min(monthdiffs)
lowincdollars = "(${:.0f})".format(lowinc)
#Identify the lowest value of the lowest decrease amount, then index that value and give the date
lowinc_min = monthdiffs.index(min(monthdiffs))
datelowinc = date[lowinc_min]
datelowinc = datelowinc.strftime("%b-%y")

#Print everything out with the lines
print("Financial Analysis")
print("------------------------------")
print("Total Months: " , num_months)
print(total_padded)
print (avgchg_padded)
print("Greatest Increase in Profits: " + (dategreatinc) + (greatincdollars) )
print("Greatest Decrease in Profits: " + (datelowinc) + (lowincdollars) )
