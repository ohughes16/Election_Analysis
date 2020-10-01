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
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
  # Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  #Read the header row
  headers = next(file_reader)

  # Print each row in the CSV file.
  for row in file_reader:
    #Add to the total vote count.
    total_votes += 1
    #A complete list of candidates who received votes
    candidate_name = row[2]
    #If the candidate does not match any existing candidate, add to candidate_options list
    if candidate_name not in candidate_options:
      #Add the candidate name to the candidate list
      candidate_options.append(candidate_name)
      #Begin tracking that candidate's vote count
      candidate_votes[candidate_name] = 0
      #Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1
  #Calculate the percentage of votes that each candidate received
  for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
      #If true then set winning_count = votes and winning percentage = vote_percentage
      winning_count = votes
      winning_percentage = vote_percentage
      #set winning_candidate equal to the candidate's name
      winning_candidate = candidate_name
  winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")
  print(winning_candidate_summary)
#Close the file
election_data.close()
