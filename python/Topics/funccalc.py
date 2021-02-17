# a simple calculator with the help of defined functions


# Sum function
def sum(x, y):
    return x + y

#sub function
def sub(x, y):
    return x - y

#div func
def div(x, y):
    return x / y

#multiplication func
def mul(x, y):
    return x * y

# absolute value
def abss(x, y):
    return str(abs(x)) + " and " + str(abs(y))


#modulus value
def mod(x, y):
    return x % y



#the operators with the help of if else

def op():
#the operator input
    inp = input("Enter your operation here: [+, -, *, /, %, abs] \n")
#the numbers be here
    num1 = int(input("The first number : "))
    num2 = int(input("The second number : "))
#for addition
    if inp == '+':
        sumr = sum(num1, num2)
        print(sumr)
#for subtraction
    elif inp == '-':
        subr = sub(num1, num2)
        print(subr)
#for multiplication
    elif inp == '*':
        multr = mul(num1, num2)
        print(multr)
#for division
    elif inp == '/':
        divr = div(num1, num2)
        print(divr)
#for modulus
    elif inp == '%':
        modr = mod(num1, num2)
        print(modr)
#for absolute value
    elif inp == 'abs':
        abssr = abss(num1, num2)
        print(abssr)
    else:
        print("Operator error!")

#end for now

#I legit forgot calling the function lmao
op()
#......... Uh... it took the input as strings u_u
#okay it works
 
