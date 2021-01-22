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

print("Checking for a word like 'whatever' in the list.")

if "whatever" in a:
     print("The list does have whatever.")
else:
     print("No the list does not have whatever in it.")


#Changing list items

print("Gonna change the last element of your list with whatever/\n")
a[-1] = "whatever/"
print('\n', a)
 #Now the first element
a[0] = "whatever@first"
print('Changing the first element as well \n', a)


#inserting an element into lists

a.insert(-1, "AddingNewWhatever@last")
print("Adding something to the last ", a)


#changing a range of elements in a list

print("Changing the values of the second to fourth element of the list.\n")
a[1:3] = ["Whatever second", "whatever third", "whatever fourth"]
print("The new list is\n", a)

