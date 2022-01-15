import pandas as pd
import numpy as np
csvfile = "../Resources/budget_data.csv"
budget_df = pd.read_csv(csvfile)
#print(budget_df.head())

# total number of months included in dataset
totalMonths = budget_df['Date'].count()
# net total of Profit/Losses
totalSum = budget_df['Profit/Losses'].sum()

# create 'Change' column and set initial value
budget_df['Change'] = 0

# change = budget_df['Profit/Losses'][i] - budget_df['Profit/Losses'][i - 1]
for i in range(1, totalMonths):
    change = budget_df['Profit/Losses'][i] - budget_df['Profit/Losses'][i - 1]
    budget_df['Change'][i] = change

# calculate average of changes in Profit/Losses
averageChange = round((budget_df['Change'].sum() / (len(budget_df) -1)), 2)

greatIncrease = budget_df['Change'].max()
greatDecrease = budget_df['Change'].min()

# set index to 'Change' and return dates of greatIncrease and greatDecrease
indexChange_df = budget_df.set_index("Change")
# print(indexChange_df.head())

increaseDate = list(indexChange_df.loc[{greatIncrease}, "Date"])
decreaseDate = list(indexChange_df.loc[{greatDecrease}, "Date"])

# print analysis to terminal
analysis = ["Financial Analysis",
"________________________",
f"Total Months: {totalMonths}", 
f"Total: ${totalSum}",
f"Average Change: ${averageChange}",
f"Greatest Increase in Profits: {increaseDate[0]} $({greatIncrease})",
f"Greatest Decrease in Profits: {decreaseDate[0]} $({greatDecrease})"]

for line in analysis:
    print(line)

# export analysis to text file
with open('analysis.txt', 'w') as file:
    file.write('\n'.join(analysis))

# print(f"Total Months: {totalMonths}")
# print(f"Total: ${totalSum}")
# print(f"Average Change: ${averageChange}")
# print(f"Greatest Increase in Profits: {increaseDate[0]} $({greatIncrease})")
# print(f"Greatest Decrease in Profits: {decreaseDate[0]} $({greatDecrease})")