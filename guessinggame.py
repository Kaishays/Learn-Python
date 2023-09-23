#create variable
secret_word = "Kai"
guess = ""
#use while loop to coniuly ask for word


guess_count = (0)
guess_limit = 3
out_of_guesses = False


#limits amount of guesses 
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit: 
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True 
if out_of_guesses: 
    print("out of guess")
else: 
    print("Success")



