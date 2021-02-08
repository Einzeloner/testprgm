#A simple regex example program becasue I am being burdened by  the college


#Python has a builtin package for RegEx called 're'
import re
x = str(input("Enter a string here: "))
#to check if the string starts with 'understandable' and ends with 'day'
y = re.search("^understandable.*day$", x)
print(bool(y))
#will print true if it satisfies the condition


#to print the list of all matches
x = str(input("Enter another string here: "))
#This will find all 'understandable' in the string
y = re.findall("understandable", x)
print(y)

