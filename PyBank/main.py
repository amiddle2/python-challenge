import csv
import os

file_path = "/Users/drewmiddleton/Desktop/Starter_Code 8/PyBank/Resources/budget_data.csv"

month_count = 0
net_profit = 0
changes = []
average_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    previous_profit = 0

    for row in csv_reader:
        month_count += 1
        net_profit += int(row[1])

        current_profit = int(row[1])
        if previous_profit != 0:
            change = current_profit - previous_profit
            changes.append(change)

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        previous_profit = current_profit

        

average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open("results.txt", "w") as file:
    
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: {net_profit}\n")
    file.write(f"Average Change: {average_change}\n")
    file.write(f"Greatest Increase: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease: {greatest_decrease_date} (${greatest_decrease})\n")
