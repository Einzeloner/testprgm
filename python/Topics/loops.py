# loops in python
# if else, for while, yada yada


#a simple if, else example
x = input("Do you know what onee sans are?[y/n] ")
#now if the statement has y as it's user input
if x == 'y':
    #Since it has y as it's input, ask this one question again.
    y = input("would you like to be dominated by an Onee san?[y/n] ")
    if y == 'y':
    #now if the input is y of the second question that was asked
        print("Ara Ara~..")
    elif y == 'n':
    #if the input is n of the second question asked
        print("Sad Ara Ara noises~...")
    else: 
    #if the input is neither of the two        
        print("Onee san demands you to enter a valid response.. HMPH..!")

#Now if the input is n for the FIRST question asked
elif x == 'n':
    #Since the output is n please do this
    z = input("State your reasons before Onee san gets mad.. Hmph! >_< ")
    print("WHAT DO YOU MEAN " + str(upper(z)))
    #this will print the response of z in upper case along with WHAT DO YOU MEAN

# if the input isn't [y/n]
else:
    print("Onee chan demands a reasonable input from you baka >_<")



