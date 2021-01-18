#defining a list then checking for the values.

a = input("First value: ")
b = input("Second value: ")
c = input("Third value: ")
d = input("Fourth value: ")
e = input("Fifth value: ")
x = [a, b, c, d, e]
#works in single mode but doesn't work in 'or' idk why.
if "1" in x:
    print("okay")
elif "7" in x:
    print("Testing again\n")
elif "3" in x:
    print("There's 3")
else:
     print("Nokay")

#Imma try if else now to see what I can do