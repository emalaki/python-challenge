import os
import csv


# File paths
election_data_csv = os.path.join("python-challenge", "PyPoll", "Resources", "election_data.csv")

output_path = os.path.join("python-challenge", "PyPoll", "analysis", "output.txt")

# Opening CSV file
with open(election_data_csv, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # Vote count (count of rows after header)
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # Create new list from "Candidate" column to get list of candidates
    candidate_list = list()
    tally = list()
    for x in range (0,row_count):
        candidate = data[x][2]
        tally.append(candidate)
        if candidate not in candidate_list: 
            candidate_list.append(candidate)
    candidate_count = len(candidate_list)

  # Votes per candidate and the percentage of total votes per candidate
    votes = list()
    percentage = list()
    for j in range (0,candidate_count):
        name = candidate_list[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct)

  # Winner based on votes per candidate
    winner = votes.index(max(votes))   


# Print and write results to output file
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candidate_count): 
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------------------")


with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {row_count:,}\n") 
    output_file.write("----------------------------\n")
    for k in range (0,candidate_count): 
        output_file.write(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {candidate_list[winner]}\n")
    output_file.write("----------------------------\n")