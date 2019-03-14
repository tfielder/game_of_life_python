class Solution():
  def set_board(self, board):
    self.board = board
    self.rows_count = len(board)
    self.columns_count = len(board[0])

  def return_board(self):
    return self.board

  def create_new_board(self):
    self.newboard = ([[0] * self.columns_count]) * self.rows_count

  def update_new_board(self, coordinates, amount):
    self.newboard[coordinates[0]][coordinates[1]] = amount

  def return_new_board(self):
    return self.newboard

  def within_range(self, coordinate, elements):
    if coordinate >= 0 and coordinate < elements:
      return True
    else:
      return False

  def get_neighbors(self):
    for row in range(self.rows_count):
      for column in range(self.columns_count):
        coordinates = [row, column]
        self.find_neighbors(coordinates)

  def find_neighbors(self, coordinates):
    neighbors = 0
    for row in range(-1 , 2):
      for column in range(-1, 2):
        first = coordinates[0] + row
        second = coordinates[1] + column
        if (self.within_range(first, self.rows_count)) and (self.within_range(second, self.columns_count)):
          if row == 0 and column == 0:
            continue
          else:
            neighbors += self.board[coordinates[0] + row][coordinates[1] + column]
    self.newboard[coordinates[0]][coordinates[1]] = neighbors
    return neighbors

  def update_board(self):
    for row in range(self.rows_count):
      for column in range(self.columns_count):
        if self.board[row][column] == 1:
          if self.newboard[row][column] <= 1 or self.newboard[row][column] >= 4:
            self.board[row][column] = 0
        if self.board[row][column] == 0 and self.newboard[row][column] == 3:
            self.board[row][column] = 1

  def run(self, board):
    self.set_board(board)
    self.create_new_board()
    self.get_neighbors()
    self.update_board()
    print(self.return_board())

def main():
  b1 = [[1,0,1],
        [1,1,1],
        [0,1,0]]

  b2 = [[1,1,1],
        [1,1,1],
        [0,1,1]]

  b3 = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

  s1 = Solution()
  s1.run(b3)

if __name__ == '__main__': main()