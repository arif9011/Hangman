def check_guess(guess):
#Guess convert to lower case
   print(guess.lower())

   # check input is valid
   if guess.isalpha() and len(guess)==1:
        print("Good guess")
    
    else :
            print(" Oops Oops! That is not a valid input.")