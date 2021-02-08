# Starting of the string topic

#Storing string inside a variable 
x = "This is how you store a string for a variable.\n" 

#printing that stored string
print(x)

#Printing string with the print command 
print("Quotations are needed.")

#printing a variable with some predefined string 
print(x + " \nAnd this is an added text")

#printing everything in lower case
print(x.lower()) #Prints the first T in lower case.


#Printing entirely in upper case
print(x.upper()) #prints everything in upper case

#checking whether the string is upper or lower case
# This will return a true or a false value.

print(x.isupper())
#It will say false because the string is not entirely in upper case.

#lets print check if a new variable is completely upper cased
y = "THIS IS ENTIRELY IN UPPER CASE!\n"
print(y)
print(y.isupper())  
#This will print the variable and check whether this is upper case or not


#same can be done with lower case characters
print(y.lower())
print(y.islower())

#combining functions for strings
print(y.upper().islower())
#will give out a false value because I just converted everything into upper

#Now time for the length of strings.
print(x + "\n{}\n".format(len(x)))
print(y + "\n{}\n".format(len(y)))

#printing a character from the given string or an input
z = str(input('Enter a string here baka >_< - '))
#I'll be printing the fifth chracter of your given string.
#Note that if there are spaces on the fifth character, it will print the space and dip.
print(z[4])

#Passing a parameter to the function and giving out different values
#remember that indexing starts at 0 instead of starting at 1
print("Printing the position of 'e' in the string that was just asked\n\n")
print(z.index("e"))
#This will only print one value and the value will be qeuivalent to the fist position of 'e'
#If I wanna print all values for the position of 'e' I'd have to use RegEx. A topic for another day


#Now we move onto replacing shit with strings
print("Anooo~ senpai... I will now replace 'e' in your string with 'C'.\nP... Please excuse me UwU\n ")
print(z.replace("e", "C"))

#This is pretty much everything to strings. Will add more as I know more.

#Okay splitting is what I missed.
split = str(input("Wanna enter a string to be split here? "))
print("I will be splitting the list at 'e'\n" + str(split.split("e")) + " UwU.\n")
