class Solution():
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
    if coordinate >= 0 and coordinate < elements:
      return True
    else:
      return False

  def get_neighbors(self):
    for i in range(self.return_rows()):
      for j in range(self.return_columns()):
        coordinates = [i, j]
        count = self.find_neighbors(coordinates)
        self.nb[j][i] = count

  def find_neighbors(self, coordinates):
    count = 0
    checks = 0
    for i in range(-1 , 2):
      for j in range(-1, 2):
        first = coordinates[0] + i
        second = coordinates[1] + j
        if (self.within_range(first, self.m)) and (self.within_range(second, self.n)):
          if i == 0 and j == 0:
            continue
          else:
            count += self.b[coordinates[0] + i][coordinates[1] + j]
    return count

  # def update_board(self):
  #   for i in range(self.return_rows()):
  #     for j in range(self.return_columns()):
  #       if self.nb[i][j] <= 1:
  #         self.nb[i][j] = 0
  #       if self.nb[i][j] >= 4:
  #         self.nb[i][j] = 0

  def run(self, board):
    self.set_board(board)
    self.create_new_board()
    self.get_neighbors()
    self.update_board()
    self.return_board()

def main():
  b1 = [[1,0,1],
        [1,1,1],
        [0,1,0]]
  b2 = [[1,0,1],[1,1,1],[0,1,0],[0,0,1]]

  s1 = Solution()
  s1.run(b1)

if __name__ == '__main__': main()



    #determine size of board
    #iterate through each cell
    #determine neighbors
    #determine if cell should live or die
    #return the board
