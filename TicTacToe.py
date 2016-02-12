
# coding: utf-8

# In[14]:

from Player import Player
from AI import AI
from Grid import Grid
import sys

def print_intro():
    print("Welcome to David's Tic Tac Toe!")
    print("The board is structured and played using (x,y) coordinates.")
    print("        y     ")
    print("    0", " ", "1", " ","2 ")
    print("  0  ","|", " ","|","    ")
    print("   ---","---","---")
    print("x 1  ","|", " ","|","    ")
    print("   ---","---","---")
    print("  2  ","|", " ","|","    ")

def get_player_type():
    good = False
    while not good:
        t = input("Is this player Human or AI? ")
        if t.lower() == "human":
            return "Human"
        if t.lower() == "ai":
            return "AI"

def get_player_icon():
    good = False
    while not good:
        t = input("Is this player 'X' or 'O'? ")
        if t.lower() == 'x':
            return "X"
        if t.lower() == 'o':
            return "O"
        
def setup(grid):
    print("Insert Player 1 information:")
    # Get Player 1 type
    player1_type = get_player_type()
    print("Player 1 is ", player1_type)
    # Get Player 1 icon 'X' or 'O'
    player1_icon = get_player_icon()
    print("Player 1 is ", player1_icon)
    
    print("Insert Player 2 information:")
    # Get Player 2 type
    player2_type = get_player_type()
    print("Player 2 is ", player2_type)
    # Player 2 icon is opposite of Player 1
    if player1_icon == 'X':
        player2_icon = 'O'
    else:
        player2_icon = 'X'
    print("Player 2 is ", player2_icon)
        
    if player1_type == 'Human':
        player.append(Player(player1_icon, grid))
    else:
        player.append(AI(player1_icon, grid))
    if player2_type == 'Human':
        player.append(Player(player2_icon, grid))
    else:
        player.append(AI(player2_icon, grid))
    
# Main
print_intro() # Print the intro and how to play
grid = Grid() # Initialize a grid
player = [] # List of players

# Create player type and icon

# Setup player types and game pieces
setup(grid)

# Keep track of move count. move_count%2 for player#'s turn. move_count>8 is a Tie
move_count = 0

# False=Continue the game True=Stop the game
winner = False

# Start game!
while not winner:
    # player1's turn
    player_id = move_count%2
    print("\n Player %d 's Turn. \n" %(player_id+1))
    if player[player_id].move():
        print("Player %d Wins!" %(player_id+1))
        winner = True
            
    # print the board
    grid.print_grid()
    
    # update total move count
    move_count = move_count + 1
    if move_count > 8:
        break
        
# check for tie game
if not winner and move_count > 8:
    print("\n Tie Game! \n")
    
print("Thank you for playing!")    
    
# End Game


# In[ ]:

player[1].piece

