import os
import csv

csvpath= os.path.join('Resources','election_data.csv')

total_votes=0
candidate_list= []
candidate= []
total_candidate_votes= {}
vote_percentage= ""
winner= ""
winner_count= 0

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile)
    
    csv_header= next(csvreader)
    
    for row in csvreader:
       # Counter for total votes
        total_votes= total_votes+1
       # Get candidates name 
        candidate= row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            total_candidate_votes[candidate]=0
        # Counter for each candidate (Total number of votes) 
        total_candidate_votes[candidate]= total_candidate_votes[candidate]+1
    print("Election Results")
    print("-------------------")
    print(f'Total Votes:{total_votes}')
    print("-------------------")
        
    for candidate in candidate_list: 
    # Percentage of votes each candidate won 
        votes= total_candidate_votes[candidate]
        vote_percentage= (votes/total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        
        if votes> winner_count:
            winner_count= votes
    # Winner of the election 
            winner= candidate
    print("--------------------")
    print(f'Winner: {winner}')
    print("--------------------")

    txtfilepath= os.path.join('analysis','electionanalysis.txt')
with open(txtfilepath,'w') as txtfile:
    txtfile.write(f'Election Results\n')
    txtfile.write(f'--------------------\n')
    txtfile.write(f'Total Votes:{total_votes}\n')
    txtfile.write("----------------------\n")
    txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txtfile.write("----------------------\n")
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write("-----------------------\n")



        
    



