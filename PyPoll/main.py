import csv
import os

csvpath = os.path.join("Resources","election_data.csv")
vote_number = 0
candidates = {}
candidate_results = []
winner = ''

def build_header():
    return "Election Results\n"\
        "----------------\n"\
        f"Total Votes: {vote_number}\n"\
        f"---------------"
        
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        vote_number += 1
        name = row[2]
        if name not in candidates.keys():
            candidates[name] = 0
        candidates[name] += 1
    
    max_votes = -1
    for candidate in candidates.keys():
        value = candidates.get(candidate)
        candidate_results.append(f"{candidate}: {round(float(value) / float(vote_number) * 100,3)}% ({value})")
        if value > max_votes:
            max_votes = value
            winner = candidate

print(build_header())
for result in candidate_results:
    print(result)
print("---------------")
print(f"Winner: {winner}")
print("---------------")

output_path = os.path.join("analysis","analysis.txt")

with open(output_path, "w") as output_file: 
    output_file.write(build_header() + "\n")
    for result in candidate_results:
        output_file.write(result + "\n")
    output_file.write("---------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("---------------")


    


    

    

