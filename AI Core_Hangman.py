import random
class Hangman:
    
    word_list: list =['apple', 'banana', 'orange', 'strawberry', 'mango']
    
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives

    word: str = random.choice(word_list)
    word_guessed: list = ['_ '] * len(word)
    num_letters: int = len(set(word))
    num_lives: int = 5
    list_of_guesses: list = []
    guess: str = ' '

   

    def check_guess(self, guess):
        guess.lower()
      
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

            for char in self.word:

                if guess == char:
                    
                    indices = [i for i, c in enumerate(self.word) if c == guess]
                    
            for number in indices:
                self.word_guessed[number] = guess

            print(self.word_guessed)  

            self.num_letters -= 1

        else:
            self.num_lives -= 1    
            print(f'Sorry, {guess} is not in the word. Try again.')
            print(f'You have {self.num_lives} lives left.')
    
    def ask_for_input(self):
        while True:
            guess = input('Enter Guess a letter: ')

            if (guess.isalpha() == False) or len(guess) != 1:
                print ('Invalid letter. Please enter a single alphabetical character.')

            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else: 
                self.check_guess(self,guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break
    

def play_game():
    num_lives = 5
    game = Hangman(Hangman.word_list, Hangman.num_lives )

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0 :
             Hangman.ask_for_input(Hangman)
        else: 
            print('Congratulations! You have won!')
            break
              
play_game()