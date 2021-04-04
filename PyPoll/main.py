import os
import csv

# analyze data
file = os.path.join("Resources","PyPoll_Resources_election_data.csv")

vote_count = 0
candidates = {}

with open(file) as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')

	header = next(csvreader)

	for vote in csvreader:
		vote_count += 1

		if vote[2] in candidates.keys():
			candidates.update({vote[2]:candidates.get(vote[2])+1})
		else:
			candidates.update({vote[2]:1})

# find winner
winner=''
winner_count=0
for i in candidates.keys():
	if candidates.get(i) > winner_count:
		winner = i
		winner_count = candidates.get(i)

# Print results
def results(candidateList):
	for i in candidateList.keys():
		print(f'{i}: {round((candidateList.get(i)/vote_count)*100,3)}% ({candidateList.get(i)})')

print('Election Results')
print('----------------------')
print(f'Total Votes: {vote_count}')
print('----------------------')
results(candidates)
print('----------------------')
print(f'Winner: {winner}')

# export as text file
output = os.path.join('Analysis','Election Results.txt')

with open(output,'a') as writer:
	writer.write(f"Election Results\n\
----------------------\n\
Total Votes: {vote_count}\n\
----------------------\n")
	
	for i in candidates.keys():
		writer.write(f'{i}: {round((candidates.get(i)/vote_count)*100,3)}% ({candidates.get(i)})\n')

	writer.write(f"----------------------\n\
Winner: {winner}")
