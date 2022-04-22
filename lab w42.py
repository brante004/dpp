from numpy import random

import random



class rpsGame():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.p1 = random.choice(self.choices)
        self.p2 = random.choice(self.choices)
        
    def manual_game(self, p1, p2):
        assert(self.p1 in self.choices and self.p2 in self.choices), 'Please input rock, paper, or scissors only'
        if p1 == p2:
            print("It's a tie")
        if p1+p2 == "rockscissors" or p1+p2 == "paperrock" or p1+p2 == "scissorspaper":
            print("Player 1 wins the game")
        if p1+p2 == "scissorsrock" or p1+p2 == "paperscissors" or p1+p2 == "rockpaper":
            print("Player 2 wins the game")

    def auto_game(self):
        if self.p1 == self.p2:
            print("It's a tie")
        if self.p1+self.p2 == "rockscissors" or self.p1+self.p2 == "paperrock" or self.p1+self.p2 == "scissorspaper":
            print("Player 1 wins the game")
        else:
            print("Player 2 wins the game")   

    def play_with_compupter(self):
        input(your_val)
        beats = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
        if beats[your_val]


rpsgame = rpsGame()
rpsgame.manual_game(p1 = 'paper', p2 = 'scissors')