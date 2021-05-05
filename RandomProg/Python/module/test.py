# a simple fibonacci program based on while loop

#fibonacci - sum of two elements defines the next

# initial value to be added 
fibinp =  1
# an initial zero value
fibinpini = 0

#an empty variable
bruh = ''
# An int number to  serve as a number till which the series is calculated
userinp = int(input("Enter an integer number here: "))

# A while loop to check the condition and apply the necessary instructions
while fibinpini < userinp:
    print(fibinpini) # print the first element 
    bruh = fibinp + fibinpini # for the next number in series as it is the sum of first two
    fibinpini = fibinp # Make the initial varibale equal to one and add further as in series 
    fibinp = bruh # Make the second varibale equal to the newly formed digit 
    


