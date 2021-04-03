# Checking whether a number is even or odd within a series

# User input for the range till which the even and odd numbers are calculated
userinp = int(input("Enter a number till which even and odd is to be calculated: "))

# A for loop to reiterate over the statement till the condition is met 
for num in range(userinp):
   #  the normal even or odd checking condition using modulus  
    if num % 2 == 0:
        print("%s is an even number." %num)
       # continue is used to go to the next instruction of the loop 
        continue
    print("%s is an odd number." %num)