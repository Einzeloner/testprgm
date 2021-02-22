# The usage of return commands in python


# usage of return commands with a defined function
def mult(x):
    return (x*x*x*x)/(x-1)
    # will raise x to the power 4 and divide it with x-1 because why not

randvar = mult(int(input("Enter a number to do some random calculations with: ")))

# Now printing the random calc variable with the help of return
print(randvar)

#Return ends a function.