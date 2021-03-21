# making a translator 


# The alpha release did what the video told me to
def translate(phrase):
   # Storing an empty value which will be used by the fucntion later in the program
    translation = ""
    for letter in phrase:
        # For a variable in the given input string please check for the next if statement
        if letter in "AEIOUaeiou":
            # So.. for loop just repeats over the statements that you provide one by one for every element.
            # If the given string has "AEIOUaeiou" the for loop will go one by one to the string and change as per the given condition
            translation = translation + "g"
        else:
            translation = translation + letter
        
    return translation


print(translate(input("Enter your string:  ")))



