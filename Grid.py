
# coding: utf-8

# In[ ]:

class Grid:
    # Create grid
    grid = []
    def __init__(self):
        self.grid = [[' ',' ',' '],
                    [' ',' ',' '],
                    [' ',' ',' ']]
    
    # Print the Tic-Tac-Toe board with pieces (if any)
    def print_grid(self):
        for i in range(2):
            print("", self.grid[i][0], "|", self.grid[i][1], "|", self.grid[i][2]) #Print tic tac toe piece
            print("---","---","---") #Print horizontal divider
        print("", self.grid[2][0], "|", self.grid[2][1], "|", self.grid[2][2]) #Print last line

    


# In[ ]:



