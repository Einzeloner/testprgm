#Basics of using numbers

#printing  a number
print(2)
print(2.0997867254748)
print(-3.564547)

#numbers and operators can be in the same print statement.
print(3*6)
print(3-6)
print(3+6)
print(3/6)

#Multiple operators
print(3*5+77)
#The interperter goes from left to right while solving equations, to alter teh flow we use parenthesis
print(3*(5+77))
#modulus function
print(10 % 3)
#prints out the remainder of the division

#Numbers can also be stored in a varible
x  = 69
print(x)

#Changing numbers into string
print(type(x))
#prints data type of the number before the conversion 
print(str(x))
#Can be useful when printing something with string
print(str(x) + " is added to this string.\n")
y = str(x) + " is added to the string."
#Now printing the data type of the whole shit in this print statemtent
print(type(y))


#Ah.. Note -  If you put anything in quotations while declaring the variable, python is gonna
# think that it is a string.

#absolute value of integer function in python.
z = -5
print("The variable declared is " + str(z))
print(str(z) + " Has an absolute value of " + str(abs(z)))
#The abs() function is used for finding an absolute value. 

# Trying it out for something with decimals
a = -2.3334454353
print("The variable declared is " + str(a) + "\n")
print(str(a) + " Has an absolute value of " + str(abs(a)))
#So absolute value is basically a mod function. like | -1 | = 1


#The pow function.
print("Printing the variable z with a power of 4 using the powe function.\n")
print("Using the pow() function the value will be " + str(pow(z, 4)) + "\n")
#This is basically equal to -5^4

#Using the max function to determine which input or variable or number has more value.
#taking user input using input
num1 = int(input("Enter two numbers from which python will determine which one has more value.: "))
num2 = int(input("Another number: "))
