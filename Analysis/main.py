import pandas as pd

csvfile = "../Resources/election_data.csv"
election_df = pd.read_csv(csvfile)
# print(election_df.head())

# total votes cast
totalVotes = election_df['Voter ID'].count()
# list of candidates
candidateList = election_df['Candidate'].unique()
# total number of votes for each candidate
voteCounts = election_df['Candidate'].value_counts()

# create variables to store candidate stats and name of election winner
candidateStats = []
electionWinner = "name"

for i in range(len(voteCounts)):
    # calculate percentage of votes each candidate won
    votePercentage = "{:.3%}".format((voteCounts[i] / totalVotes))
    # collect and store calculations for each candidate
    candidateStats.append(f"{candidateList[i]}: {votePercentage} ({voteCounts[i]})")
    # find overall winner
    if voteCounts[i] == voteCounts.max():
        electionWinner = candidateList[i]


# print analysis to terminal
analysis = ["Election Results", 
"---------------", 
f"Total Votes: {totalVotes}", 
"---------------", 
candidateStats[0],
candidateStats[1],
candidateStats[2],
candidateStats[3],
"---------------", 
f"Winner: {electionWinner}"]

for line in analysis:
    print(line)

# export analysis to text file
with open('analysis.txt', 'w') as file:
    file.write('\n'.join(analysis))