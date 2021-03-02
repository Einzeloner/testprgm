#A simple python dictionary program.

#A dictionary is enclosed in '{}' while a list is enclosed in '[]'


#defining a dictionary
x = {"FirstElement": "OneeChan", "SecondElement": "Hazukashii", "ThirdElement": "baka!", "FourthElement": ">_<"}

#Printing a dictionary element with the name defined and the index
print(str(x["FirstElement"]) + "\nCannot print with indexing in dictionaries lol.\n") 

#Finding out the length of this dictionary
print("The length of this dictionary is " + str(len(x)))


# Month conversion type of deal
mcinput = input("Enter the first three letters of your month: ")

# The dictionary for the month conversion
md = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

# Now to print the fucking months
print(md.get(mcinput))