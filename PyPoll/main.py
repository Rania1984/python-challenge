
# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list={}

# Winning Candidate and Winning Count Tracker
winner = ""
winner_votes = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list[candidate] = 1
        else:

        # Add a vote to the candidate's count
            candidate_list[candidate] += 1

#Open a text file to save the output
with open(file_to_output, 'w') as file:

    print(f"Election Results\n")
    print("------------------------\n")

    file.write(f"Election Results\n")
    file.write("------------------------\n")

    #Print the total vote count (to terminal)
    print(f"Total votes: {total_votes}\n")
    print("------------------------\n")

    # Write the total vote count to the text file
    file.write(f"Total votes: {total_votes}\n")
    file.write("------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_list.items():

        # Get the vote count and calculate the percentage
        percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.2f}% ({votes})\n")
        file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")

        if votes > winner_votes:
            winner_votes=votes
            winner=candidate

    # Generate and print the winning candidate summary

    print("------------------------\n")
    print(f"winner: {winner}\n")

    # Save the winning candidate summary to the text file

    file.write("------------------------\n")
    file.write(f"winner: {winner}\n")

