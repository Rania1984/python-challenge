**PyBank challenge:**

I used ChatGPT to help me by answering questions, explaining code concepts, and suggesting solutions specifically in the below section
# Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = date

# Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = date

I also got help from my husband with the below codes I wasn'nt sure how to write it:
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------------------\n")
    txt_file.write(f"Total months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")


**PyPoll challenge:**

I wasn't sure how to use `print(". ", end="")` in the code so I ended up using regular lines (----) instead."
also in this challenge my husband helped me with how to finalize the code with printing to the terminal
and writing the results to the text file.
