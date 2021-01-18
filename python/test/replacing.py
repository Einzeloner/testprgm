# Replacing multiple strings inside of the program

x = raw_input("Enter string: ")
if 'f' in x:
    print(x.replace('f', 'd'))
elif 'F' in x:
    print(x.replace('F', 'D'))
else:
    print('NOO!')
