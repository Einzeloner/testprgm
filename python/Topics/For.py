# A sample program for a for loop in python

lstring = input("Enter a string to be printed vertically: ")
# The  for loop is used to print letters one by one
for  fuck in lstring:
    print(fuck)

# The same can be done for arrays and can also be  used when speciiying ranges to print
somearr = ["Uzaki", "Hana", "Nagatoro", "Asuna", "Miku"]
print("\n\nSo the defined array is  this\n", somearr)

# Now to print this one by one
for whateverthefuck in somearr:
    print(whateverthefuck)

# for loop looks for the variable no matter  the name  and prints the letters or elements one by  one because of the print command
#printing some number from 1 to the number - 1 one buy one using for loop

num = int(input("Enter a number to be printed line by line: "))

for somerandbs in range(num):
    print(somerandbs)

# well the first run gave me an error saying int is not iterable lmao
# oh okay, for printing the numberline you have to use  the range function.
# yeah okay this run finally works .


# same can be done with numbers in a certain range 
rlower = int(input("Lower limit of the range: "))
rupper = int(input("Upper limit of the range: "))

for absolutebullfuck in range(rlower, rupper):
    print(absolutebullfuck)


