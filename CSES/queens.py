board = []
  
def check_collisions(row, col):
    # Mark vertically
    r, c = row, col
    for i in range(len(board)):
        if board[i][c] == "X":
            return False

    # Mark diagonally right
    r, c = row, col
    while c >= 0 and c <= 7 and r >= 0 and r <= 7:
        if board[r][c] == "X":
            return False
        r -= 1
        c += 1

    # Mark diagonally left
    r, c = row, col
    while c >= 0 and c <= 7 and r >= 0 and r <= 7:
        if board[r][c] == "X":
            return False
        r -= 1
        c -= 1

    return True

def search(n_queens):

    if n_queens == 8:
        return 1
    
    tally = 0
    for i in range(8):
        if board[n_queens][i] == "*":
            continue
        if check_collisions(n_queens, i):
            board[n_queens][i] = "X"
            tally += search(n_queens+1)
            board[n_queens][i] = "."
    
    return tally

for i in range(8):
    board.append(list(input()))

print(search(0))
