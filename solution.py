class Solution():
  def run(self, board):
    response = "r"
    while response != "q":
      self.set_board(board)
      self.welcome_message()
      self.create_new_board()
      self.check_for_neighbors()
      self.update_board()
      self.print_board()
      x = input()

  def welcome_message(self):
    print("Welcome to Conway's Game of Life")
    print("1s represent living cells, zeros represent non-living cells")
    print("Your board starts like this:")
    self.print_board()
    print("Press the spacebar to iterate through each moment in time.")
    print("Type 'q' to quit at any point.")

  def set_board(self, board):
    self.board = board
    self.rows_count = len(board)
    self.columns_count = len(board[0])

  def create_new_board(self):
    self.newboard = ([[0] * self.columns_count]) * self.rows_count

  def check_for_neighbors(self):
    for row in range(self.rows_count):
      for column in range(self.columns_count):
        coordinates = [row, column]
        neighbors =self.find_neighbors_at_coordinate(coordinates)
        self.update_new_board(coordinates, neighbors)

  def update_new_board(self, coordinates, neighbors):
    self.newboard[coordinates[0]][coordinates[1]] = neighbors

  def find_neighbors_at_coordinate(self, coordinates):
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
    return neighbors

  def within_range(self, coordinate, elements):
    if coordinate >= 0 and coordinate < elements:
      return True
    else:
      return False

  def update_board(self):
    for row in range(self.rows_count):
      for column in range(self.columns_count):
        if self.board[row][column] == 1:
          if self.newboard[row][column] <= 1 or self.newboard[row][column] >= 4:
            self.board[row][column] = 0
        if self.board[row][column] == 0 and self.newboard[row][column] == 3:
            self.board[row][column] = 1

  def print_board(self):
    print('')
    for row in range(self.rows_count):
        print(self.board[row])
    print('')

def main():
  b1 = [[1,0,1],
        [1,1,1],
        [0,1,0]]

  b2 = [[1,1,1],
        [1,1,1],
        [0,1,1]]

  b3 = [[0,1,0],
        [0,1,1],
        [1,0,1],
        [1,1,0]]

  s1 = Solution()
  s1.run(b3)

if __name__ == '__main__': main()