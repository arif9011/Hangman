import random
word_list =['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango']
random.choice
# pick a random choice from a list of strings.
word=random.choice(word_list)
print(word)
guess=input("Enter a single letter :  ")
print(guess)

def check_guess(guess):
#Guess convert to lower case
   print(guess.lower())

   # check input is valid
   if guess.isalpha() and len(guess)==1:

        print("Enter is valid")
   else:
     print(" Oops Oops! That is not a valid input.")

            #Enter is in word
     if guess in word :

                print("Good.  {guess} is the word")
                
     else:
                print("opps! invalid guess")
