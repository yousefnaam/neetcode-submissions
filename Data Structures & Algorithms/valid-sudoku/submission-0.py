class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #have a set for row, col, and 3x3 grid, we check if it is in set
        # if they are currently in any set, then return false
        #if we make it to the end of the board, return true

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        return True
                




        