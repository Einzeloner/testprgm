# Output and Input formatting in python

# Output formatting

# declaring two random variables with string and int input respectively 
string = "Some random text"

integer = 34

# Using f or F before the starting of strong quotation allows us to write python expression between {}
a = f'This is an example of how {string} looks with {integer}'
print(a)

# the str.format() method,
# used because more control over the output in the string
num1 = 2233445566
num2 = 6677885588.4343434343
# with the normal F formatting
print(f"{num1} might or might not be greater than {num2}")
# Now with the str.format()
b = '{:0} is the last 5 digits from num1 and {:4.3} are the 4 digits before decimal and 5 digits after decimal\
 from num2'
 
print(b.format(num1, num2))