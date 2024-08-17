import os
import csv

# Initialize variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_changes = []
average_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Read the CSV filecsvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Calculate total months and total profit
        total_months += 1
        total_profit += int(row[1])

        # Calculate profit change
        current_profit = int(row[1])
        if previous_profit != 0:
            change = current_profit - previous_profit
            profit_changes.append(change)
        previous_profit = current_profit

# Calculate the average change
average_change = sum(profit_changes) / len(profit_changes)

# Calculate the greatest increase in profit (date and amount) over the entire period
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Calculate profit change
        current_profit = int(row[1])
        if previous_profit != 0:
            change = current_profit - previous_profit
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
        previous_profit = current_profit

# Calculate the greatest decrease in profits (date and amount) over the entire period
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Calculate profit change
        current_profit = int(row[1])
        if previous_profit != 0:
            change = current_profit - previous_profit
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        previous_profit = current_profit


# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit:}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date}, $({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}, $({(greatest_decrease)})")

# Open a new file for writing the results
output_file_path = os.path.join('PyBank', 'Analysis', 'financial_analysis_results.txt')
with open(output_file_path, 'w') as file:
#with open('PyBank' 'Analysis' 'financial_analysis_results.txt', 'w') as file:
    # Write the analysis results to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits:  {greatest_increase_date}, $({greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date}, $({greatest_decrease})\n")
