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