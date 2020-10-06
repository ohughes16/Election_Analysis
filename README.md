# Election Analysis

## Project Overview
A Colorado Board of Elections employee has tasked me to complete an election audit of a recent local congressional election.
I was asked to complete the following:
1. Calculate the total number of votes
2. Provide a list of candidates who received votes
3. Calculate the total number of votes that each candidate received
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Provide a breadown of the number of votes and the percentage of total votes for each county in the precinct.
7. Determien the county that had the largest number of voters.

## Resources

- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.49.2

## Summary
The analysis of the election showed that:
- There were 369,711 votes cast in the election
- The candidates were: 
    - Charles Casper Stockham: 23.0% (85,213)
    - **Diana DeGette: 73.8% (272,892)**
    - Raymon Anthony Doane: 3.1% (11,606)
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The breakdown of county votes:
    - Jefferson County: 10.5% (38,855)
    - **Denver County: 82.8% (306,055)**
    - Arapahoe County: 6.7% (24,801)
    
 **Denver County cast the highest number of votes.**
 
## Election-Audit Summary
This script was designed to run through a .csv file of election results. The script is coded to skip the header row and the columns are hard coded to be specific values. The 1st column in the .csv is ignored, the second column in the .csv (index 1) is pulled as the "County" variable, and the third column in the .csv (index 2) is pulled as the candidate names.

```ruby
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
 ```
If you are going to re-use this code for another election, be sure to modify either the index in the election_data IO you are referencing, or ensure that the .csv is formatted the same as the election_results.csv that was provided for this analysis.

There are a couple of modificaitons that could be done to this code to shorten the code and make it more intuitive. Instead of creating lists for candidate_options and county_list, we could shorten the code and call on the dictionary keys. 

Also in this particular code for the winning county decision statement we could eliminate the 'and' conditional and our results would be the same since the highest number of votes would still be the winner, regardless of the percentage of votes that individual received. If this would change in the future, we could modify the code to indicate that.
```ruby
for county in county_votes:
        # 6b: Retrieve the county vote count.
        voter_turnout = county_votes.get(county)
        # 6c: Calculate the percent of total votes for the county.
        county_vote_percentage = float(voter_turnout) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({voter_turnout:,})\n"
        ) 
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (voter_turnout > current_winning_count) and (county_vote_percentage > current_winning_percentage):
            current_winning_count = voter_turnout
            winning_county = county
            current_winning_percentage = county_vote_percentage
```
