set1={"one","two","three"}
set2={"two","three","four","five"}
set3={1,2,3,4,5,6,7,8,9}
set4={4,5,6,7}
set5={1,2,3}
set6={4,5,6}

#printing all sets
print("set1: ",set1)
print("set2: ",set2)
print("set3: ",set3)
print("set4: ",set4)
print("set5: ",set5)
print("set6: ",set6)



# Union
print("Union: ",set1|set2)
print(set1.union(set2))

#intersection
print("Intersection: ",set1&set2)
print(set1.intersection(set2))
#symmetric Difference
print("Symmetric Difference: ",set1^set2)
print(set1.symmetric_difference(set2))

#Difference 
print("Difference: ",set1-set2)
print(set1.difference(set2))

# Updates set1 with set2
set1.update(set2)
print(set1)

#symmetric difference update
set2.symmetric_difference_update(set1)
print(set2)

#adds element to set1
set1.add("addElement")
print(set1)

#difference update
set1.difference_update(set2)
print(set1)


#clears set1
set1.clear()
print(set1)

#removes element "two" in set2
set2.discard("two")
print(set2)

#copy
x=set2.copy()
print(x)


#subset
print("is set4 subset of set3: ",set4.issubset(set4))

#superset
print("is set3 superset of set4: ",set3.issuperset(set4))

#pop
set2.pop()
print("Set4 after pop:",set4)

print("set2:",set2)
#remove 
set2.remove("five")
print("set2 after element 'five' is removed: ",set2)

#is dijoint
print("is set5 and set6 are in Disjoint: ",set5.isdisjoint(set6))



#Loop print sets
print("Printing sets using for loop")
for i in set3:
    print(i)


