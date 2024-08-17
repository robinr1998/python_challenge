import os
import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Calculate total votes
        total_votes += 1

        # Add candidate to the dictionary if not already in the dictionary
        candidate = row[2]  # Candidate names are in the 3rd column
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export the results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Export the results to a text file
output_file_path = os.path.join('PyPoll', 'Analysis', 'election_results.txt')
with open(output_file_path, 'w') as file:
    for result in results:
        file.write(result + "\n")
