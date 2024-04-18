import csv
import os

file_path = "/Users/drewmiddleton/Desktop/Starter_Code 8/PyPoll/Resources/election_data.csv"

total_votes = 0
candidates = []
ccs_votes = 0
ccs_percent = 0
dd_votes = 0
dd_percent = 0
rad_votes = 0
rad_percent = 0
winner = ''


with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  

    for row in csv_reader:
        total_votes += 1

        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
        if row[2] == 'Charles Casper Stockham':
            ccs_votes += 1
        elif row[2] == 'Diana DeGette':
            dd_votes += 1
        elif row[2] == 'Raymon Anthony Doane':
            rad_votes += 1

    ccs_percent = (ccs_votes / total_votes) * 100.0
    dd_percent = (dd_votes / total_votes) * 100.0
    rad_percent = (rad_votes / total_votes) * 100.0
        
    if dd_percent > rad_percent and dd_percent > ccs_percent:
        winner = 'Diana DeGette'
    elif rad_percent > dd_percent and rad_percent > ccs_percent:
        winner = 'Raymon Anthony Doane'
    elif ccs_percent > rad_percent and ccs_percent > dd_percent:
        winner = 'Charles Casper Stockham'
    else:
        winner = 'tie!'

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f'Charles Casper Stckham: {ccs_percent:.3f}% ({ccs_votes})')
    print(f'Diana DeGette: {dd_percent:.3f}% ({dd_votes})')
    print(f'Raymon Anthony Doane: {rad_percent:.3f}% ({rad_votes})')
    print("----------------------------")
    print(f'Winner: {winner}')
    print("----------------------------")
