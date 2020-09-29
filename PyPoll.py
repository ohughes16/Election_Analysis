# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name2": votes}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
         #2. Add to the total vote count.
       total_votes += 1

       #2. A complete list of candidates who received votes
       candidate_name = row[2]
       
       #If the candidate does not match any existing candidate, add to candidate_options list
       if candidate_name not in candidate_options:
           
           candidate_options.append(candidate_name)

print(candidate_options)   


#3. Total number of votes each candidate received

#4. Percentage of votes each candidate won

#5. The winner of the election based on popular vote

#Close the file
election_data.close()
