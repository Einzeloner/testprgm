print("For a 3x3 set\n")
set1a = int(input("Enter set1's number a: "))
set1b = int(input("Enter set1's number b: "))
set1c = int(input("Enter set1's number c: "))
set1 = {set1a, set1b, set1c}
print("set 1 - ", set1)

set2a = int(input("Enter set2's number a: "))
set2b = int(input("Enter set2's number b: "))
set2c = int(input("Enter set2's number c: "))
set2 = (set2a, set2b, set2c)
print("set 2 - ", set2)

print("Enter the operation\n |  = union\n & = Intersection\n ^ = Symmetric difference\n ")

op = input("Enter your operation: ")
if op == "|":
    print( "Intersection = \n", set1 | set2)
elif op =="&":
    print("Intersection = \n", set1 & set2)
elif op == "^":
    print("Syemmetrical difference = \n", set1 ^ set2)

else print("Invalid operation\n")
