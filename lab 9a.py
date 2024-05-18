#Charles Huang

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

outcomes = {
    ('rock', 'rock'): "It's a tie!",
    ('rock', 'paper'): "P2 wins!",
    ('rock', 'scissors'): "P1 wins!",
    ('paper', 'rock'): "P1 wins!",
    ('paper', 'paper'): "It's a tie!",
    ('paper', 'scissors'): "P2 wins!",
    ('scissors', 'rock'): "P2 wins!",
    ('scissors', 'paper'): "P1 wins!",
    ('scissors', 'scissors'): "It's a tie!"
    }

p1 = input('Pick one of rock, paper or scissors: ')

def choice():
    p2 = random.choice(choices)




def game(games):
    p1_wins = 0
    p2_wins = 0
    ties = 0
    for i in range(games):
        x = input('Pick one of rock, paper or scissors: ')
        y = random.choice(choices)
        print (f"P1: {x}, P2: {y}")
        print(outcomes[(x, y)])
        if outcomes[(x, y)] == "P1 wins!":
            p1_wins += 1
        elif outcomes[(x, y)] == "P2 wins!":
            p2_wins += 1
        elif outcomes[(x, y)] == "It's a tie!":
            ties += 1
        else:
            break
    print(f"There were {p1_wins} wins for P1, {p2_wins} wins for P2, and {ties} ties.")
    
game(10)
    
#Now update to allow 0 or 2 human players


#For human players, they need to be able to choose a play each turn inside the loop


def multiplayer(human_players, games):
    p1_wins = 0
    p2_wins = 0
    ties = 0
    
    def player_test():
        if human_players == 0:
            x = random.choice(choices)
            y = random.choice(choices)
    
        elif human_players == 1:
            x = input('Pick one of rock, paper or scissors: ')
            y = random.choice(choices)

        elif human_players == 2:
            x = input('Pick one of rock, paper or scissors: ')
            y = input('Pick one of rock, paper or scissors: ')

        return x, y        


    for i in range(games):
        x, y = player_test() #remember, player_test returns two variables
        print (f"P1: {x}, P2: {y}")
        print(outcomes[(x, y)])
        if outcomes[(x, y)] == "P1 wins!":
            p1_wins += 1
        elif outcomes[(x, y)] == "P2 wins!":
            p2_wins += 1
        elif outcomes[(x, y)] == "It's a tie!":
            ties += 1
        else:
            break
    print(f"There were {p1_wins} wins for P1, {p2_wins} wins for P2, and {ties} ties.")   
    
multiplayer(0, 10)
multiplayer(2, 3)
 

        
        
