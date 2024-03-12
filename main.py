import random

class GuessNumberGame:
    def __init__(self, min_num = 1, max_num = 1000):
        self.min_num = min_num
        self.max_num = max_num
        self.random_number = random.randint(self.min_num, self.max_num)
        
    def user_guess(self):
            while True:
                try:
                    guess = int(input(f'Guess a number between {self.min_num} and {self.max_num}: '))
                    if self.min_num <= guess <= self.max_num:
                        return guess
                    else:
                        print(f'Your guess should be between {self.min_num} and {self.max_num}. Please try again.')
                except ValueError:
                    print('Invalid input. Please enter a number.')
        
    def play(self):
            while True:
                user_guess = self.user_guess()
                if user_guess < self.random_number:
                    print('Sorry, guess again. Too low.')
                elif user_guess > self.random_number:
                    print('Sorry, guess again. Too high.')
                else:
                    print(f'Congratulations! You have guessed the number {self.random_number} correctly!')
                    break
                
                
if __name__ == "__main__":
    game = GuessNumberGame()
    game.play()
