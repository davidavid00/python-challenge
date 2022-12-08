import os
import csv

poll_path = os.path.join("Resources", "election_data.csv")

#declairation of variables
voteCount = 0
tVoteCount = 0
cCandidate = ""
winner = ""
results = {}
candidatevotes = []
votepercentage = []

#function to count votes
def countVote(candidate):
    if candidate in results:
        #add a vote to the results dictionary
        results[candidate] +=1
    else:
        #create a new key with the value in one in results dictionary
        results[candidate] = 1


#open csv
with open(poll_path, encoding="utf")as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    #for every row, count the vote and send to countVote function
    for vote in csvreader:
        tVoteCount+=1
        cCandidate = vote[2]
        countVote(cCandidate)

candidatelist = list(results.keys())

#for each candidate in results, add their votes to a list [candidatesvotes]
for i in results:
    candidatevotes.append(results[i])
    #calculate the precentage of votes received
    votepercentage.append(results[i]/tVoteCount*100)

#print results to terminal
print("Election Results")
print("--------------------------")
print(f'Total Votes: {tVoteCount}')
print("--------------------------")
print(f"{candidatelist[0]}: {votepercentage[0]:.3f}% ({candidatevotes[0]})")
print(f"{candidatelist[1]}: {votepercentage[1]:.3f}% ({candidatevotes[1]})")
print(f"{candidatelist[2]}: {votepercentage[2]:.3f}% ({candidatevotes[2]})")
print("Winner: ", max(results, key=results.get))
print("--------------------------")

#print results to a txt
with open('PyPolloutput.txt', 'w') as output:
    output.write("Election Results\n")
    output.write("--------------------------\n")
    output.write(f'Total Votes: {tVoteCount}\n')
    output.write("--------------------------\n")
    output.write(f"{candidatelist[0]}: {votepercentage[0]:.3f}% ({candidatevotes[0]})\n")
    output.write(f"{candidatelist[1]}: {votepercentage[1]:.3f}% ({candidatevotes[1]})\n")
    output.write(f"{candidatelist[2]}: {votepercentage[2]:.3f}% ({candidatevotes[2]})\n")
    output.write("Winner: ") 
    output.write(max(results, key=results.get))
    output.write("\n--------------------------")