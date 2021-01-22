# Operations on lists

#defining lists

a = ["some element", "some string in quotations", 4, 6, "Numbers without the quotation may work"]
print(a)

#taking input from the user and defining a list that way

x = input("First element: ")
y = input("Second element: ")
z = input("Third element: ")
f = input("Fourth element: ")
g = input("last element: ")

a = [x, y, z, f, g]
print(a)

#operations on lists

#accessing items from list

j = print("First element is {}", x)
if j in a:
     print("Yeah this is the first element ", j)
