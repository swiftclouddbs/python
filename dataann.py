#Dataannotation test script - called dataann.py
#Script takes a dictionary consisting of number/word pairs and
#returns the words mapped to a unique number
#first line in input file begins with 195 land
#Description follows the code
#At Step 5, enter the number(s) desired to show the matching word(s).

#Load libraries here, such as pandas, matplotlib, etc.  Path
#is needed to help this Mac find the datafile

from pathlib import Path

#Step 1
#set some variables to ease reading and writing of code
data_folder = Path("/Users/reginaldstuart/Documents/python")

file_to_open = data_folder / "data.txt"

#Step 2
#open the file containing the data to process
open_file = open(file_to_open, 'r')

#Step 3
#take the data in the file and create a dictionary called data
data = {}
for line in open_file:
    val, keys = line.strip().split(' ', 1)
    data.update(dict.fromkeys(keys.split(' '), val))

#Step 4
#reverse the key/value relationship so that we have everything in a format we like
rev_data = {}
for key, value in data.items():
    rev_data.setdefault(value, []).append(key)
    
#Step 5
#get the records/data we want
first = rev_data['1']
second = rev_data['3']
third = rev_data['6']

#Step 6 
#put our desires into a single tuple
sample = (first, second, third)

#Step 7
#crack the tuple
sample2 = first[0],second[0],third[0]

#Step 8
#print the string requested by the Boss.
print(*sample2)
