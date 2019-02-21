#For a space that is 'populated':
#Each cell with one or no neighbors dies, as if by solitude.
#Each cell with four or more neighbors dies, as if by overpopulation.
#Each cell with two or three neighbors survives.
#For a space that is 'empty' or 'unpopulated'
#Each cell with three neighbors becomes populated.

#input = [[1,0,1],
         #  [0,1,1],
         #  [1,1,0]
         # ]

class Solution:

    def run(self, board):
        def set_board(self, board):
          self.b = board
          self.m = len(board)
          self.n = len(board[0])

        def return_board(self):
          return self.b

        def return_rows(self):
          return self.m

        def return_columns(self):
          return self.n

        def create_new_board(self):
          self.nb = ([[0] * self.n]) * self.m

        def update_new_board(self, coordinates, amount):
          self.nb[coordinates[0]][coordinates[1]] = amount

        def return_new_board(self):
          return self.nb

        def within_range(self, coordinate, elements):
          if coordinate > 0 and coordinate < elements:
            return True
          else:
            return False

        def find_neighbors(self, coordinates):
          count = 0
          for i in range(-1 , 2):
            for j in range(-1, 2):
              first = coordinates[0] + i
              second = coordinates[1] + j

              if (within_range(self, first, self.m)) and (within_range(self, second, self.n)):
                if i == 0 and j == 0:
                  continue
                else:
                  #print(coordinates)
                  #print(self.b[coordinates[0] + i][coordinates[1] + j])
                  count += self.b[coordinates[0] + i][coordinates[1] + j]
          return count

        def get_coordinates(self):
          for i in range(return_rows(self)):
            for j in range(return_columns(self)):
              coordinates = [i, j]
              find_neighbors(self, coordinates)
              amt = find_neighbors(self, coordinates)
              #print(amt)
              #update_new_board(self, coordinates, amt)




        def update_new_board(self):
          return self.nb

        set_board(self, board)
        create_new_board(self)
        return_new_board(self)
        get_coordinates(self)

        #return_board(self)
b1 = [[1,0,1],[1,1,1],[0,1,0]]
b2 = [[1,0,1],[1,1,1],[0,1,0],[0,0,1]]

s1 = Solution()
s1.run(b1)



    #determine size of board
    #iterate through each cell
    #determine neighbors
    #determine if cell should live or die
    #return the board
