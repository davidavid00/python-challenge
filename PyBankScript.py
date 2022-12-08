import os
import csv

budget_path = os.path.join ("Resources", "budget_data.csv")

#Declaration of variables
rowcount = 0
totalpl = 0
prevPL = 0
change = 0.0
listOfChange = []
gIncrease = 0
gIncreaseMonth = ""
gDecrease = 0
gDecreaseMonth = ""

#open the csv
with open(budget_path, encoding="utf")as csvfile:
    csvreader = csv.reader(csvfile)
    #skip header
    header = next(csvreader)
    
    #loop for each row of the csv
    for row in csvreader:
        rowcount+=1
        
        #add profit/loss
        totalpl = totalpl + int(row[1])

        if rowcount > 1:
            change = prevPL + int(row[1])
            #if change is the greatest, set a new value for gIncrease
            if change > int(gIncrease):
                gIncrease = change
                gIncreaseMonth = row[0]
            #if loss is the highest, set a new value for gDecrease
            elif change < int(gDecrease):
                gDecrease = change
                gDecreaseMonth = row[0]
            #add the change to a list
            listOfChange.append(change)
        #set the previous value as negative
        prevPL = -int(row[1])
    
    #find the avereage of 
    avgChange = sum(listOfChange)
    avgChange = round(int(avgChange) / (rowcount-1), 2)

#print results in the terminal
print("Financial Analysis")
print("--------------------------")
print(f'Total Months: {rowcount}')
print(f'Total: {totalpl}')
print(f'Average Change: {avgChange}')
print(f'Greatest Increase in Profits: {gIncreaseMonth} (${gIncrease})')
print(f'Greatest Decrease in Profits: {gDecreaseMonth} (${gDecrease})')

#print the results to a txt
with open('PyBankoutput.txt', 'w') as output:
    output.write("Financial Analysis \n")
    output.write("-------------------------- \n")
    output.write(f'Total Months: {rowcount}\n')
    output.write(f'Total: {totalpl}\n')
    output.write(f'Average Change: {avgChange}\n')
    output.write(f'Greatest Increase in Profits: {gIncreaseMonth} (${gIncrease})\n')
    output.write(f'Greatest Decrease in Profits: {gDecreaseMonth} (${gDecrease})\n')
