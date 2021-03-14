# Maybe a guessing game

secword = "whatever"
# an empty guess variable 
guess = ""
# The count of the guesses that a user has made 
guess_count = 0
# The limit for the guesses 
guess_limit = 3

# While the condition in the while loop matches,  run the code again and
while guess != secword:
    if guess_count < 3:
        guess = input("Enter guess: ") 
        guess_count += 1
    else:
        print("Out of guesses!")
        break
    if guess_count == 3:
        print("You lose!")
        break
    if  guess == secword:
        print("You win!")
# print("You win")