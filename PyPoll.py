# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
# Import the datetime class from the datetime module.

#writing a code - first always import a module - csv will allow to work with data stored in csv file
import csv
#import os to use the os.path module to get to the file path
import os
#before opening a file to read we need to assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis','election_analysis.txt')

#open the election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function
    file_reader = csv.reader(election_data)
 # Read and print the header row.
    headers = next(file_reader)
    print(headers)



