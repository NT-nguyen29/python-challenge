# import os module
import os

# module for reading csv files
import csv

csvpath = os.path.join("Resources/budget_data.csv")

with open(csvpath) as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
