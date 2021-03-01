# Comparisions with if else

# the number greater than the most

# number one
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))

# now the fucn that will do all of the job

def maxnum():
    if n1 >= n2 and n1 >= n3:
        print("%d is the greatest" %n1)

    elif n2 >= n1 and n2 >= n3:
        print("%d is the greatest" %n2)

    else:
        print(n3)

# now for calling the function
maxnum()


# Now to see if the strings are the same with the help of random fuck shit
s1 = input("First fuking string here: ")
s2 = input("Another fucking string here: ")
s3 = input("one more string: ")

def lenstring():
   if len(s1) >= len(s2) and len(s1) >= len(s3):
        print(s1, " has the greatest string length")

   elif len(s2) >= len(s1) and len(s2) >= len(s3):
       print(s2, " has the greatest string length")

   else:
        print(s3, " Has the greatest string length")

lenstring()
