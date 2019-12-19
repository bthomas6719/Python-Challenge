#Importing the necessary modules/libraries

import os
import csv
from collections import Counter
#Creating an object out of the CSV file
poll_data = os.path.join("PythonData", "election_data.csv")
count = 0
candidates = []
poll_result = []
vote_count = Counter()
vote_percent = []


#Opening and reading the CSV file
with open(poll_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reading the header row
    csv_header = next(csvreader)
    
    #Reading the first row (so that we track the changes properly)
    for row in csvreader:
        #candidate names to list
        candidates.append(row[2])
    totalVotes = len(candidates)

    #find candidate names
    for name in (candidates):
        vote_count[name] += 1
    
    winner = tuple(vote_count.keys())
    names = tuple(vote_count.keys())
    votes = tuple(vote_count.values())

    for value in votes:
        vote_percent.append((int(value)/totalVotes)*100)
    poll_result.append('Election Results')
    poll_result.append('-------------------------')
    poll_result.append('Total Votes: ' + str(totalVotes))
    poll_result.append('-------------------------')

    for x in range(len(names)):
        poll_result.append(names[x] + ': ' + str(round(vote_percent[x],2)) + '00% ' + '(' + str(votes[x]) + ')')
    poll_result.append('-------------------------')
    poll_result.append('Winner: ' + winner[0])
    poll_result.append('-------------------------')
    print('\n'.join((poll_result)))

    
