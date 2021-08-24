
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for row in board:
            for i in range(1,10):
                if row.count(str(i))>1:
                    return False

        for i in range(9):
            for j in range(i,9):
                board[i][j],board[j][i]=board[j][i],board[i][j]
    
        
        for row in board:
            for i in range(1,10):
                if row.count(str(i))>1:
                    return False

        for i in range(9):
            for j in range(i,9):
                board[i][j],board[j][i]=board[j][i],board[i][j]

        subgrids = []
        for box_i in range(3):
            for box_j in range(3):
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        subgrid.append(board[3*box_i + i][3*box_j + j])
                subgrids.append(subgrid)

        for row in subgrids:
            for i in range(1,10):
                if row.count(str(i))>1:
                    return False

        return True
        


b = input()
board = eval(b)

# board = board.reshape(1,-1)

# print(type(board.tolist()))

# print(type(board))
# for i in board:
#     for j in i:
#         print(j)
ii = 1
for i in board:
  
    for j in board[board.index(i)]:
        print(ii,j)
        ii+=1
test = Solution

print(test.isValidSudoku(test,board))



[[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]

[['.', '.', '4', '.', '.', '.', '6', '3', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['5', '.', '.', '.', '.', '.', '.', '9', '.'],
['.', '.', '.', '5', '6', '.', '.', '.', '.'],
['4', '.', '3', '.', '.', '.', '.', '.', '1'],
['.', '.', '.', '7', '.', '.', '.', '.', '.'],
['.', '.', '.', '5', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.']]