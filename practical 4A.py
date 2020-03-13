# Pytho program to show regular expressions
# Importing re module
import re

txt = "The rain in Spain"
# Search the string to see if it starts with "The" and ends with "Spain"
x = re.search("^The.*Spain$", txt)
print("Search:"+str(x))

# Print a list of all matches
x = re.findall("ai", txt)
print("Find All:"+str(x))

# Return an empty list if no match was found
x = re.findall("Portugal", txt)
print("Find All:"+str(x))

# Search for the first white-space character in the string
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
print("Split:"+str(x))

# Split the string only at the first occurrence
x = re.split("\s", txt, 1)
print(x)

# Replace every white-space character with the number 9
x = re.sub("\s", "9", txt)
print(x)

# Replace the first 2 occurrences
x = re.sub("\s", "9", txt, 2)
print(x)
