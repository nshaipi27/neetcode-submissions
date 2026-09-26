class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for j in range(cols):
            seen = set()
            for i in range(rows):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        square = [['', '', ''], ['','',''], ['','','']]

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True