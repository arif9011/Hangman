def check_guess(guess):
#Guess convert to lower case
   print(guess.lower())

   # check input is valid
   if guess.isalpha() and len(guess)==1:

        print("Enter is valid")
   else:
     print(" Oops Oops! That is not a valid input.")

            #Enter is in word
     if guess in word:

                print("Good.  {guess} Enter the word")
                
     else:
                print("opps! invalid guess")
