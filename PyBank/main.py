import csv
import os
csvpath = os.path.join("Resources","budget_data.csv")

number_of_months = 0
profit = 0
average_change = 0
increase_date = ''
decrease_date = ''
increase = 0
decrease = 0

def build_output():
    return "Financial Analysis\n"\
           "--------------------------------\n"\
           f"Total Months: {number_of_months}\n"\
           f"Total: ${profit}\n"\
           f"Average Change: {average_change}\n"\
           f"Greatest Increase in Profits: {increase_date} (${int(increase)})\n"\
           f"Greatest Decrease in Profits: {decrease_date} (${int(decrease)})"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    changes = []
    dates = []
    not_is_first_row = False
    previous = 0
    for row in csvreader:
        number_of_months += 1
        profit += int(row[1])
        if not_is_first_row:
            changes.append(float(row[1]) - previous)
            dates.append(row[0])
        previous = float(row[1])
        not_is_first_row = True
    
    total = float(0)
    for change in changes:
        total += change 
    average_change = total / float(len(changes))

    increase = changes[0]
    decrease = changes[0]

    for i in range(0,len(changes)):
        if changes[i] > increase:
            increase = changes[i]
            increase_date = dates[i]
        if changes[i] < decrease:
            decrease = changes[i]
            decrease_date = dates[i]
    
    print(build_output())

output_path = os.path.join("analysis","analysis.txt")
with open(output_path, "w") as output_file: 
    output_file.write(build_output())






       
    