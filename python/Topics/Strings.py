# Starting of the string topic

#Storing string inside a variable 
print("Storing a string inside a variable: \n\n")
x = "This is how you store a string for a variable." 

#printing that stored string
print(x)
print("\n\n         x = 'somestring'\n              print(x)\n ")

#Printing string with the print command 
print("Quotations are needed.")

#printing a variable with some predefined string 
print("Adding some string with the predefined variable.\n\n")
print(x + " \nAnd this is an added text")

#printing everything in lower case
print("Printing everything in lower case.\n\n")
print(x.lower()) #Prints the first T in lower case.


#Printing entirely in upper case
print("Printing everything in upper case.\n\n")
print(x.upper()) #prints everything in upper case

#checking whether the string is upper or lower case
# This will return a true or a false value.
print("Checking whether the value is upper case or not.\n\n")
print(x.isupper())
#It will say false because the string is not entirely in upper case.

#lets print check if a new variable is completely upper cased
y = "THIS IS ENTIRELY IN UPPER CASE!"
print(y)
print(y.isupper())  
#This will print the variable and check whether this is upper case or not


#same can be done with lower case characters
print(y.lower() + " \nsike!")
y = "Boolean value for checking if the string value is lower or not.\n\n" 
print(y)
print(y.islower())

#now combining the two functions and checking that way with a new string variable
z = "This MaY Be lOwER Or uPpEr idfk\n"
print(z + "\n\n")
print(z.upper())
print(z.upper().isupper())
#same for lower case
print(z.lower())
print(z.lower().islower())

#Now for finding the length or the number of characters in a string
print("Finding the length of the variables x,y and z.\n\n")
print(x + "\n{}\n".format(len(x)))
print(y + "\n{}\n".format(len(y)))
print(z + "\n{}\n".format(len(z)))



