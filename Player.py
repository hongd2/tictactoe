
# coding: utf-8

# In[ ]:

class Player:
    piece = ' '
    grid = []
    
    # Construct a player with piece='X' or 'O', grid=Grid Object
    def __init__(self, piece, grid):
        self.piece = piece
        self.grid = grid
    
    # Print piece 'X' or 'O'
    def print_piece(self):
        print(self.piece)
   
    # Print instruction and store coordinate
    def get_coordinate(self):
        good = False
        
        # Check validity
        while not good:
            x = int(input("Please enter the x coordinate you want to move (x=[0:2]): "))
            if not self.check_valid(x):
                print("Invalid Location. Please move somewhere valid x=[0:2] y=[0:2].")
                continue
            y = int(input("Please enter the y coordinate you want to move (y=[0:2]): "))
            if not self.check_valid(y):
                print("Invalid Location. Please move somewhere valid x=[0:2] y=[0:2].")
                continue
                
            good = self.check_occupancy(x, y)
            
            if not self.check_occupancy(x, y):
                print("Space is occupied. Please move somewhere else.")
                
        return x, y
    
    # Check valid location
    def check_valid(self, point):
        if point < 0 or point > 2:
            return False
        return True
    
    # Check occupancy
    def check_occupancy(self, x, y):
        if self.grid.grid[x][y] != ' ':
            return False
        return True
        
    # Return True if winner is found
    def move(self):
        (x, y) = self.get_coordinate()
        self.grid.grid[x][y] = self.piece
        if self.check_winner():
            return True
            
        return False
    
    # Check all possible orientations (8 ways: 3 rows, 3 columns, 2 diagonals)
    def check_winner(self):
        # 3 rows
        if self.grid.grid[0][0] == self.grid.grid[0][1] == self.grid.grid[0][2] == self.piece:
            return True
        if self.grid.grid[1][0] == self.grid.grid[1][1] == self.grid.grid[1][2] == self.piece:
            return True
        if self.grid.grid[2][0] == self.grid.grid[2][1] == self.grid.grid[2][2] == self.piece:
            return True
        # 3 columns
        if self.grid.grid[0][0] == self.grid.grid[1][0] == self.grid.grid[2][0] == self.piece:
            return True
        if self.grid.grid[0][1] == self.grid.grid[1][1] == self.grid.grid[2][1] == self.piece:
            return True
        if self.grid.grid[0][2] == self.grid.grid[1][2] == self.grid.grid[2][2] == self.piece:
            return True
        # 2 diagonals
        if self.grid.grid[0][0] == self.grid.grid[1][1] == self.grid.grid[2][2] == self.piece:
            return True
        if self.grid.grid[0][2] == self.grid.grid[1][1] == self.grid.grid[2][0] == self.piece:
            return True
        return False
        


# In[ ]:



