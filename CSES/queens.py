from copy import deepcopy

def printArray(board):
    for i in board:

        for j in i:
            print(j, end=" ")
        print()
    
def in_bounds(board, pos):
    r,c  = pos
    hb1, hb2 = 0, len(board[0])-1
    vb1, vb2 = 0, len(board)-1
    return (c >= hb1 and c <= hb2) and (r >= vb1 and r <= vb2)

def find_valid(board):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==".":
                moves.append((i,j))
    return moves

def mark_board(pos, board):
    # pos > (row,column)
    # Mark vertically
    r, c = pos
    for i in range(len(board)):
        board[i][c] = "*"

    # Mark horizontally
    for i in range(len(board[0])):
        board[r][i] = "*"

    # Mark diagonally left
    cur_pos = (r,c)
    while in_bounds(board, cur_pos):
        board[cur_pos[0]][cur_pos[1]] = "*"
        cur_pos = (cur_pos[0]+1, cur_pos[1]-1)
    
    cur_pos = (r,c)
    while in_bounds(board, cur_pos):
        board[cur_pos[0]][cur_pos[1]] = "*"
        cur_pos = (cur_pos[0]-1, cur_pos[1]+1)

    # Mark diagonally right

    cur_pos = (r,c)
    while in_bounds(board, cur_pos):
        board[cur_pos[0]][cur_pos[1]] = "*"
        cur_pos = (cur_pos[0]+1, cur_pos[1]+1)
    
    cur_pos = (r,c)
    while in_bounds(board, cur_pos):
        board[cur_pos[0]][cur_pos[1]] = "*"
        cur_pos = (cur_pos[0]-1, cur_pos[1]-1)

    return board

def search(n_queens, board, tally):

    if n_queens == 8:
        return tally+1
    
    valid = find_valid(board)

    for i,j in valid:
        tally = search(n_queens+1, mark_board((i,j), deepcopy(board)), tally)
    
    return tally

board = []

for i in range(8):
    board.append(list(input()))

print(search(0, board, 0))