# -----------------------knight-------------------------------------
# game settings b6
knight_moves = [[-1, 2], [-1, -2], [1, 2], [1, -2],
                [-2, 1], [-2, -1], [2, -1], [2, 1]]
board_letters = 'abcdefgh'
n = 8

# getting initial knight position
coord = list(input())
col_0 = board_letters.index(coord[0])
row_0 = n - int(coord[1])

# setting the board with the knight on it
chess_board = [['.' for _ in range(n)] for _ in range(n)]
chess_board[row_0][col_0] = 'N'

# filling in knight possible knight moves
for row, col in knight_moves:
    i = row_0 + row
    j = col_0 + col
    if n > i >= 0 and n > j >= 0:
        chess_board[i][j] = '*'

# drawing the knight position and available moves
for row in chess_board:
    print(*row)


# -----------------------QUEEN-------------------------------------
# board settings
board_letters = 'abcdefgh'
n = 8

# getting initial Queen's position
coord = list(input())
col_0 = board_letters.index(coord[0])
row_0 = n - int(coord[1])

# drawing board with Queen moves
chess_board = [['*' if i == row_0 or j == col_0
                or i+j == row_0+col_0
                or i-j == row_0-col_0
                else '.'
                for j in range(n)]
               for i in range(n)]

# placing the Queen
chess_board[row_0][col_0] = 'Q'

# drawing the result
for row in chess_board:
    print(*row)
