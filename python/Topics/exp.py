# making an exponential function in python with the help of for loop 


# Define two variables for the parameters

base = int(input("Enter the base number of the exp function: ")) 
power = int(input("Enter the power of the base number: "))

def expfunc(base, power):
     ans = 1  
     for fuck in range(power):
        ans =  ans * base
     return ans

print(expfunc(base, power))



# idk what happened but when I put 1 instead of the ans the program just doesn't work for some reason
# my understanding would be that the 1 is doing some shit and not lettting the for loop continue but I can be horribly wrong

