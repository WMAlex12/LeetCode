import collections 

def isValidSudoku(board):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    square = collections.defaultdict(set)

    for r in range(9): 
        for c in range(9): 
            if board == ".": 
                continue
            if (board [r][c]) in rows[r] or (board [r][c]) in rows[c] or (board [r][c]) in square[r//3,c//3]: 
                return False
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        square[(r//3,c//3)].add(board[r][c])
    return True