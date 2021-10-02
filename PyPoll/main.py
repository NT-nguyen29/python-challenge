# import os module
import os

# module for reading csv files
import csv

csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath) as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    # loop through data
    for row in csvreader:
    
        

