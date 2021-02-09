#For the functions in python

#Most of the functions will be defined in the individual programs. This is
#just some random bs


#The sorted function
x = ["A", "C", "B", "c", "z", "1", "2"]
print("The list to be sorted- " + str(x))
z = sorted(x)
print("The sorted list-\n" + str(z))
#This sorts Numbers > UPPER CASE CHARS > lower case chars


#user defined functions
#for defining a function use the 'def' function and then function name
def shotakun():
    x = input("Would you like to be dominated by an onee san? [y/n] ")
    if x == 'y':
        print("Ara Ara~...")
    elif x == 'n':
        print("Sad Onee san noises .....\n")
    else:
        print("Onee san is not happy about that you know.. Hmph!\n")

#This program will ask for your input and display the print statement
#results accordingly.

#Now to actually use that function you just go...
shotakun()


#passing arguments in the defined function