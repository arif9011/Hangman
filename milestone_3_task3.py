import random
word_list =['Apple', 'Banana', 'Orange', 'Strawberry', 'Mango']
random.choice
# pick a random choice from a list of strings.
word=random.choice(word_list)

guess=input("Enter a single letter :  ")
print(guess)

def check_guess(guess):
#Guess convert to lower case
   guess.lower()

            #Enter is in word
if guess in word :

        print(f"Good guess! {guess} is the word")
                
else:
       print("opps! invalid guess")

       ##check_guess(guess)          
        
def ask_for_input():
     while True: 
      guess=input(" Enter your guess :")  
      check_guess(guess)
      if guess.isalpha()==False and len(guess)==1:
             print("Invalid letter. Please, enter a single alphabetical character.")
      else: 
            print(" Enter Character is valid")
            break       
        
            return ask_for_input()
ask_for_input()

        
               