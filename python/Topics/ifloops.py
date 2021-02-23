# A really simple example of if elese loops


# using a user defined function to explain if else
def somefunc():
    x = input("Would you like to create a list or a tuple?[l/t] ")
    # now the if condition for if the statement has the response l
    if  x == "l":
        print("So you want to print a list.(5 elements)")
        e1 = input("First element: ")
        e2 = input("Second element: ")
        e3 = input("Third element: ")
        e4 = input("Fourth element: ")
        e5 = input("Fifth element: ")
        # list1 variable will be the list of all elements
        list1 = [e1, e2, e3, e4, e5]
    # if the response of the user is 't'. elif stands for else if
    elif x == 't':
        print("So you want to print a tuple.(5 elements)")
        t1 = input("First element: ")
        t2 = input("First element: ")
        t3 = input("First element: ")
        t4 = input("First element: ")
        t5 = input("First element: ")
        # tup1 is the tuple of all elements
        tup1 = (t1, t2, t3, t4, t5)
    # Else if nothing matches just end the function
    else:
        print("Please enter a valid response baka! >_<")

# Now call that function and ask the user if the user wants to print the function
    
uinp = input("Would you like to print your desired input?[y/n] ")
if uinp == 'y':
    somefunc()
else:
    print("program exiting now")
