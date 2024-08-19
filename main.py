
#import csv file
import os
import csv

#path to csv
csvpath = '/Users/cristianwaitman/Desktop/Challenge 3/PyBank/Resources/budget_data.csv'

# Lists to store data
date = []
profit_losses = []
changes = []
great_increase = []
great_decrease = []

#open csv file using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    next(csvreader)
  
    #start loop
    for row in csvreader:
        # Add date column
        date.append(row[0])
        # Add profit losses column
        profit_losses.append(int(row[1]))
        

#calculate total months
total_months = len(date)

#calculate net total profil losses
net_total = sum(profit_losses)


# Initialize variables for greatest increase
greatest_increase_value = 0
greatest_increase_date = ''

# Initialize variables for greatest decrease
greatest_decrease_value = 0
greatest_decrease_date = ''


# Changes in "Profit/Losses"
for i in range(1, len(profit_losses)):
    change = profit_losses[i] - profit_losses[i - 1] #compares the curent value vs last value
    changes.append(change) #adds changes


    # Check if change is the greatest increase
    if change > greatest_increase_value:
        greatest_increase_value = change
        greatest_increase_date = date[i]    

    # Check if change is the greatest decrease
    if change < greatest_decrease_value:
        greatest_decrease_value = change
        greatest_decrease_date = date[i]   


# Calculate the average of profit/losses + 2 decimals
average_change = round(sum(changes) / len(changes), 2)  


# Store the greatest increase in the list
great_increase = [greatest_increase_date, greatest_increase_value]

# Store the greatest decrease in the list
great_decrease = [greatest_decrease_date, greatest_decrease_value]


#prints
analysis = (
    "Financial Analysis\n"


    " --------------------------- \n"


    f"Total Months: {total_months}\n"


    f"Total: {net_total}\n"


    f"Average Change: ${average_change}\n"


    f"Greatest Increase in Profits: {great_increase[0]} (${great_increase[1]})\n"


    f"Greatest Decrease in Profits: {great_decrease[0]} (${great_decrease[1]})\n"
)
    


print(analysis)

# Export prints to a text file
output_path = '/Users/cristianwaitman/Desktop/Challenge 3/PyBank/Analysis/PyBank_analysis.txt'

with open(output_path, 'w') as text_file:
    text_file.write(analysis)