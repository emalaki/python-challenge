import os
import csv

#File path
budget_data_csv = os.path.join("/Users/ellenmalaki/python-challenge/PyBank/Resources/budget_data.csv")

#Output path
txtfile_path = "/Users/ellenmalaki/python-challenge/PyBank/output.txt"

#Variables
months_count = 0
revenue_count = 0
revenue = []
original_rev = 0
month = []
rev_dif = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
rev_change = []
avg_rev = 0


with open("/Users/ellenmalaki/python-challenge/PyBank/Resources/budget_data.csv") as csvfile:  
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        months_count += 1

        revenue_count = revenue_count + int(row["Profit/Losses"])

        rev_dif = float(row["Profit/Losses"])- original_rev
        original_rev = float(row["Profit/Losses"])
        rev_change = rev_change + [rev_dif]
        month = [month] + [row["Date"]]



        if rev_dif > greatest_increase[1]:
            greatest_increase[1] = rev_dif
            greatest_increase[0] = row["Date"]


        if rev_dif < greatest_decrease[1]:
            greatest_decrease[1] = rev_dif
            greatest_decrease[0] = row["Date"]


    avg_rev = sum(rev_change)/len(rev_change)




    print("Financial Analysis\n")
    print("---------------------\n")
    print("Total Months: %d\n" % months_count)
    print("Total Revenue: $%d\n" % revenue_count)
    print("Average Revenue Change $%d\n" % avg_rev)
    print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))



with open(txtfile_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % months_count)
    file.write("Total Revenue: $%d\n" % revenue_count)
    file.write("Average Revenue Change $%d\n" % avg_rev)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))




    
