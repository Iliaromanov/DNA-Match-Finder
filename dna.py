from sys import argv, exit
import csv

# ensure user gives exactly three command line arguments
if len(argv) != 3:
    print("Usage: dna.py {database} {sequence}")
    exit(1)

# open the dna database file and copy the information into a dictionary called database
# the names of the persons will be the keys of the dict and an array of their repeating DNA sequences will be the values
with open(argv[1]) as csvfile:
    database = {}
    reader = csv.DictReader(csvfile, fieldnames = ['name'], restkey = "seq")
    for row in reader:
        database[row['name']] = row['seq']


# open the dna sequence file and save the sequence as a string
with open(argv[2], "r") as seq:
    dna = ""
    for nucleotide in seq:
        dna += nucleotide
