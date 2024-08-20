#import csv file
import os
import csv

#path to csv
csvpath = '/Users/cristianwaitman/Desktop/Challenge 3/PyPoll/Resources/election_data.csv'


# Lists to store data
balotes = []
candidate = []

# Dictionary to store candidate votes
candidate_votes = {}

#open csv file using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    next(csvreader)

    #start loop
    for row in csvreader:
        # Add date column
        balotes.append(row[0])
        # Add profit losses column
        candidate.append(row[2])

        # If candidate is in dictionary, increment their vote count
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
        else:
            # If candidate is not in dictionary, add them with a vote count of 1
            candidate_votes[row[2]] = 1



#calculate total votes
total_votes = len(balotes)

# list of candidates 
unique_candidates = list(candidate_votes.keys())

# percentage of votes per candidate
candidate_percentages = {candidate: round((votes / total_votes) * 100, 3) for candidate, votes in candidate_votes.items()}

#candidate with more votes
winner = max(candidate_votes, key=candidate_votes.get)



#prints

analysis = (
    "Election Results\n\n"


    " --------------------------- \n\n"


    f"Total Votes: {total_votes}\n\n"


    " --------------------------- \n\n"
)

#for loop to retrieve candidate name, percentage & total votes
for candidate, percentage in candidate_percentages.items():
    analysis += f"{candidate}: {percentage}% ({candidate_votes[candidate]} votes)\n\n"

analysis += (

    " --------------------------- \n\n"


    f"Winner: {winner}\n\n"

    " --------------------------- \n"
)
    

print(analysis)


# Export prints to a text file
output_path = '/Users/cristianwaitman/Desktop/Challenge 3/PyPoll/Analysis/PyPoll_analysis.txt'

with open(output_path, 'w') as text_file:
    text_file.write(analysis)