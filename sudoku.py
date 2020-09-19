def solve(board):
    find = empty_position(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid_position(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def valid_position(board, position, num):
    for i in range(0, len(board)):
        if board[position[0]][i] == num and position[1] != i:
            return False

    for i in range(0, len(board)):
        if board[i][position[1]] == num and position[1] != i:
            return False

    box_x = position[1]//3
    box_y = position[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False
    return True


def empty_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")
            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")

example_board = [ [0,1,2,0,0,0,8,0,6],
                  [0,0,0,8,0,0,2,1,0],
                  [0,0,0,0,0,6,5,0,7],
                  [5,3,9,0,0,0,0,0,0],
                  [4,0,1,0,0,0,0,0,3],
                  [8,0,0,9,0,1,0,0,0],
                  [2,0,3,0,7,0,0,0,0],
                  [0,0,0,0,8,3,7,9,0],
                  [0,0,0,4,0,0,3,0,5]]

solve(example_board)
print_board(example_board)
