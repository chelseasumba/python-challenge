import os
import csv

csvpath= os.path.join('Resources','election_data.csv')

total_votes=0
candidates= []
percentage_candidate_votes= 
total_candidate_votes= {}
winner= ""

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile)
    print(csvreader)
    
    csv_header= next(csvreader)
    print(f'CSV Header:{csv_header}')
    

    for row in csvreader:
         # Get candidates name 
        candidates= row[2]
        

        # Counter for total votes

        # Counter for each candidate (Total number of votes) 

        # Add each county to the list 

        # Percentage of votes each candidate won 

        # Winner of the election 


print(f'Election Results')
print('-----------------------')
print(f'Total Votes: {}')
print('-----------------------')

for item in candidate:
    print(f'{item}: ')

        
    



