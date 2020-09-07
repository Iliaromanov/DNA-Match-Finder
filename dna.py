from sys import argv, exit
import csv

# ensure user gives exactly three command line arguments
if len(argv) != 3:
    print("Usage: dna.py {database} {sequence}")
    exit(1)

# load the dna database into memory as a dictionary
# the names of the persons will be the keys of the dict and an array of their repeating DNA sequences will be the values
with open(argv[1]) as csvfile:
    database = {}
    reader = csv.DictReader(csvfile, fieldnames = ['name'], restkey = "seq")
    for row in reader:
        database[row['name']] = row['seq']

# load the dna sequence into memory as a string
with open(argv[2], "r") as seq:
    dna = ""
    for nucleotide in seq:
        dna += nucleotide


def count_string_repeat(string: str, text: str) -> int:
    """ Counts max amount of times a substring repeats consecutively in a given string
        
        Args:
            string(str): the substring
            text(str): the string
            
        Return:
            int: a count of the max amount of times the substing appears consecutively
    """
    count = 0
    pattern = string
    while pattern in text:
        count += 1
        pattern += string
    return count


def search_database(database: dict, dna: str) -> str:
    """ Searches provided database dict for matching sequences of Short Tandum Repeats (STRs)
    
        Args:
            database(dict): a dictionary with persons names as keys and lists of STR counts as values
            dna(string): the dna sequence of an unknown person
            
        Returns:
            string: the name of the person who matches the STR counts in the database or 'No match' if there is no match
    """
    # make and populate an array for counts of STRs
    STRs = []
    for seq in database['name']:
        STRs.append(count_string_repeat(seq, dna))
    
    # search database for matching array of STR counts
    for person in database:
        if database['person'] == STRs:
            return person

    return "No match"
    