
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
changes = []
previous_profit_loss = None

greatest_increase_amount = 0
greatest_increase_date = ""

greatest_decrease_amount = 0
greatest_decrease_date = ""


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list

    # Track the total and net change


    # Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Track the total
        total_months += 1

      # Track the net change
        total_net += profit_loss

        if previous_profit_loss is not None:
            change= profit_loss-previous_profit_loss
            changes.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = date

            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = date

        previous_profit_loss=profit_loss

# Calculate the average net change across the months
average_change=sum(changes)/len(changes)

# Generate the output summary
# Print the output
print("Financial Analysis")
print("-------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------------------\n")
    txt_file.write(f"Total months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

