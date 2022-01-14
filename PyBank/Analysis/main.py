import pandas as pd
import numpy as np
csvfile = "../Resources/budget_data.csv"
budget_df = pd.read_csv(csvfile)
#print(budget_df.head())

totalMonths = budget_df['Date'].count()
totalSum = budget_df['Profit/Losses'].sum()

# change = budget_df['Profit/Losses'][i] - budget_df['Profit/Losses'][i - 1]
budget_df['Change'] = 0

for i in range(1, totalMonths):
    change = budget_df['Profit/Losses'][i] - budget_df['Profit/Losses'][i - 1]
    budget_df['Change'][i] = change
    # change = 0

print(budget_df.head())

# print(averageChange)
averageChange = round((budget_df['Change'].sum() / (len(budget_df) -1)), 2)

greatIncrease = budget_df['Change'].max()
greatDecrease = budget_df['Change'].min()

if budget_df['Change'][i] == greatIncrease:
    increaseDate = budget_df['Date'][i]
elif budget_df['Change'][i] == greatDecrease:
    decreaseDate = budget_df['Date'][i]


# print(f"Total Months: {totalMonths}")
# print(f"Total: ${totalSum}")
# print(f"Average Change: ${averageChange}")
# print(greatIncrease)
# print(greatDecrease)
print(increaseDate)
