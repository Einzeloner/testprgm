#x = int(input("Your number here: "))
#fac = 1
#if x == 0:
#    fac = 1
#    print('Factorial of', x, 'is', fac)
#elif x > 0:
#    for i in range(1, x + 1):
#        fac = fac * i
#        print("Factorial of", x, "is", fac)
#    else: print("Not a valid number")



x = int(input("Your number here: "))
factorial = 1
if x<0:
    print("Not a valid number")
elif x==0:
    print("The factorial is 1")
else:
    for f in range(1, x + 1):
        factorial = factorial*f
        print("Factorial = ", factorial)
