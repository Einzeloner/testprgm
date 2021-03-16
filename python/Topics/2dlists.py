# Python can do this cool thing where it can store lists under lists and whatnot

# so basically if you wanna make a matri x and want to store everything else while being able to access them
# in like a grid matrix pattern you an go with 2d lists

# Lemme change the color theme cause it is fucking hard to read these comments

#defining a 4x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# now to print an element let's say 3rd row 2nd( 2nd coloumn) element 
print(matrix[2][1])
# it printed 12 at the first try because I forgot that the indexing starts at 0

# printing the whole matrix using the for  loop
for fuck in matrix:
    print(fuck)

# printing the whole matrix one by one using for loop
for hit in matrix:
    for fuck in hit:
        print(fuck)

# if you do `for fuck in matrix` in line 26 then it will print out the whole matrix 4 times because 4 elements in the list
