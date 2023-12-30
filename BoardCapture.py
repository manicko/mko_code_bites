class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        ln = len(board)
        for i in range(ln):
            for j in range(ln):
                if board[i][j] == 'R':
                    x0, y0 = i, j
                    break
        res = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j

            while 0 <= x < ln and 0 <= y < ln:
                if board[x][y] == 'p':
                    res += 1

                if board[x][y] != '.':
                    break

                x, y = x + i, y + j

        return res    
sol=Solution()
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
res = sol.numRookCaptures(board)
print(res)


