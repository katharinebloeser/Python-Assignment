import os

import csv

#Find the csv file
csvpath=os.path.join("..","MODULE 3 ASSIGNMENT","PyPoll", "Resources","election_data.csv")
#Create the variables I will use throughout, this list was created in an iterative process
Ballot=[]
County=[]
Candidate=[]
unique_candidates = set()
VotesforRAD = []
VotesforCCS = []
VotesforDD= []
percentofvoteRAD=[]
percentofvoteCCS=[]
percentofvoteDD=[]
VotesforRAD = 0
VotesforCCS=0
VotesforDD=0

#Import the csv file
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
#Skip the header row
    next(csvreader)
#Create variables for each candidate, counting the number of ballots (i.e., rows) per candidate
    for row in csvreader:
        Ballot.append(int(row[0]))
        Candidate=row[2]
        unique_candidates.add(Candidate)
        if Candidate == "Raymon Anthony Doane":
            VotesforRAD+=1
        elif Candidate == "Charles Casper Stockham":
            VotesforCCS+=1
        elif Candidate =="Diana DeGette":
            VotesforDD+=1
#ChatGPT--I got help for the +=1 code   

#Find the total number of rows (i.e., ballots), then calculate the percentage of the vote for each candidate using that value
numvotes=len(Ballot)
percentofvoteRAD = VotesforRAD/numvotes*100
percentRAD = "{:.3f}%".format(percentofvoteRAD)
RADpad = "({:.0f})".format(VotesforRAD)
#got help for the format code from StackOverFlow

percentofvoteCCS = VotesforCCS/numvotes*100
percentCCS = "{:.3f}%".format(percentofvoteCCS)
CCSpad = "({:.0f})".format(VotesforCCS)

percentofvoteDD = VotesforDD/numvotes*100
percentDD = "{:.3f}%".format(percentofvoteDD)
DDpad = "({:.0f})".format(VotesforDD)

#The three candidates are Raymon Anthony Doane, Charles Casper Stockham, and Diana DeGette
#for candidate in unique_candidates:
#    print(candidate)      
           
print("Election Results")
print("-------------------------")
print("Total Votes: ", numvotes)
print("-------------------------")
print("Charles Casper Stockham: ", (percentCCS), (CCSpad))
print("Diana DeGette: ", (percentDD), (DDpad))
print("Raymon Anthony Doane: ", (percentRAD), (RADpad))
print("-------------------------")
print("Winner: Diana DeGette")
print("-------------------------")
