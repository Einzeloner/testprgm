# A simple if else program with or as it's condition

# A simple input data type checker

# A variable for the input data type
inp1 = input("Enter the datatype here: [int/float/str]")
if inp1 == 'int':
    print("A number entered here will be checked for even or odd (int).")
    # A variable to ask for your number
    num1 = int(input("Enter your number here: "))
    if (num1 % 2) == 0:
        print("Yep the number is even because %f is divisible by 2 with it's quotient being " + str(num1/2), num1)

# Now for the same variable but in float condition
elif inp1 == 'float':
    print("Your data type is float and idk what to do tbh.\n end of thinking capacity")
    print("Jk... I will think of something else.. I think...")
    num2 = float("Enter a float number here: ")
    print("Your int to float conversion results in " + str(int(num2)))

#else if the input is string 
elif inp1 == 'string':
    str1 = str(input("enter the string here or something idk..: "))
    print("Will convert everything to upper case now\n")
    print(str1.upper())

# Else if nothing matches just end the code and tsay input not found
else:
    print("Please enter a valid input")

