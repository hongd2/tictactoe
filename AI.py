
# coding: utf-8

# In[1]:

from Player import Player
class AI(Player):
#     This class extends Player
#
#
#     check_valid(point) Returns True if the proposed singular point is within the constraints [0:2]
#     def check_valid(self, point):
#         if point < 0 or point > 2:
#             return False
#         return True
#    
#     check_occupancy(x, y) Returns True if the proposed coordinate is vacant
#
#     def check_occupancy(self, x, y):
#         if self.grid.grid[x][y] != ' ':
#             return False
#         return True
#
#
#     move() Returns True if winner is found
#
#     def move(self):
#         (x, y) = self.get_coordinate()
#         self.grid.grid[x][y] = self.piece
#         if self.check_winner():
#             return True
#            
#         return False


    # When AI is constructed in TicTacToe.py, the below move() overrides the inherited move().
    #
    # Add your own AI here, making sure that you use check_valid and check_occupancy.
    # Or override those two functions yourself.
    #
    # My AI algorithm just finds the first available spot to put a mark.
    
    def move(self):
        for x in range(3):
            for y in range(3):
                if not self.check_valid(x) or not self.check_valid(y) or not self.check_occupancy(x, y):
                    continue
                self.grid.grid[x][y] = self.piece
                if self.check_winner():
                    return True
                return False
        
                
                


# In[ ]:



