#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
bank_data = os.path.join("PythonData", "budget_data.csv")
total_months = 0
total_profit_loss = 0
value = 0
change = 0
month = []
profits = []

#Opening and reading the CSV file
with open(bank_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reading the header row
    csv_header = next(csvreader)
    
    #Reading the first row to record the changes 
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])

    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the months
        month.append(row[0])
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        #Total number of months
        total_months += 1


        #Total amount of profit/loss over entire period"
        total_profit_loss = total_profit_loss + int(row[1])

    #Greatest increase months/profits 
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_month = month[greatest_index]

    #Greatest decrease months/profits
    greatest_decrease = min(profits)
    lowest_index = profits.index(greatest_decrease)
    lowest_month = month[lowest_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)


#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_month} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {lowest_month} (${str(greatest_decrease)})")



# opens the output destination in write mode and prints the summary
with open('newBudget','w') as writefile:
    writefile.writelines('\n')
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Profits: $' + str(total_profit_loss) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(round(avg_change,2)) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + (greatest_month) + ' ($' + str(greatest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + (lowest_month) + ' ($' + str(greatest_decrease) + ')')



#opens the output file in r mode and prints to terminal
with open('newBudget', 'r') as readfile:

    print(readfile.read())
