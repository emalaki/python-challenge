import os
import csv

# File paths
budget_data_csv = os.path.join("python-challenge", "PyBank", "Resources", "budget_data.csv")

output_path = os.path.join("python-challenge", "PyBank", "analysis", "output.txt")

# Variables
months_count = 0
revenue_count = 0
prev_month_revenue = 0
month_revenue_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

# Read CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        # Count number of months
        months_count += 1

        # Sum revenue
        revenue_count += int(row[1])

        # Calculate revenue change
        month_revenue = int(row[1])
        if months_count > 1:
            revenue_change = month_revenue - prev_month_revenue
            month_revenue_change.append(revenue_change)
            if revenue_change > greatest_increase[1]:
                greatest_increase = [row[0], revenue_change]
            if revenue_change < greatest_decrease[1]:
                greatest_decrease = [row[0], revenue_change]
        prev_month_revenue = month_revenue

# Calculate average revenue change
avg_rev_change = sum(month_revenue_change) / len(month_revenue_change)

# Print and write results to output file
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {months_count}")
print(f"Total Revenue: ${revenue_count}")
print(f"Average Revenue Change: ${avg_rev_change:.2f}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")


with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {months_count}\n")
    output_file.write(f"Total Revenue: ${revenue_count}\n")
    output_file.write(f"Average Revenue Change: ${avg_rev_change:.2f}\n")
    output_file.write(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")