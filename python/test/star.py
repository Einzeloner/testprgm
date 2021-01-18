x = int(input("Number of stars that you want to print: "))
print("Printing in backwards pattern...\n")
for i in range(x,0,-1):
    print((x -i)* ' ' + i * '*' )
