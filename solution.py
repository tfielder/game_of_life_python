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
    m = 0
    n = 0
    b = []

    def set_board(board):
        self.b = board

    def return_board(board):
        return board

    def set_board_size(board):
        m = len(board)
        n = len(board[0])

    def run(self, board):
        set_board(self, board)
        get_board_size(board)
        return "True"

    #determine size of board
    #iterate through each cell
    #determine neighbors
    #determine if cell should live or die
    #return the board
