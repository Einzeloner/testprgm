#Input from a user.

x = input("Enter something baka >_<! ")
#checking to see if the input was registered
print("A..An..Anone senpai... You wrote s.. something like... " + str(x) + " UwU.\n")


#Building a basic calculator.
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

#operations start here
z = str(input("""\nInput your operation here: 
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus: """))


#For addition if the variables
if z == '+':
    print("Senpai Senpai the addition will be " + str(x + y) + " UmU.\n")
#for subtraction of variables
elif z == '-':
    print("Senpai Senpai the subtraction will be " + str(x - y) + " UmU.\n")
#for multiplication
elif z == '*':
    print("Senpai Senpai the multiplication will be " + str(x * y) + " UmU.\n")
#for division
elif z == '/':
    print("Senpai Senpai the division will be " + str(x / y) + " UmU.\n")
#for modulus
elif z == '%':
    print("Senpai Senpai the modulus will be " + str(x % y) + " UmU.\n")
#If nothing matches
else:
    print("Uhhh senpai.... Operator is not supported u_u.\n")

#Okay done with the whole program
print("Calculated ig..")