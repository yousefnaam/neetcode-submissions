class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        gridset = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                current = board[r][c]
                if current == ".":
                    continue
                if current in rowset[r] or current in colset[c] or current in gridset[(r // 3, c // 3)]:
                    return False
                else:
                    rowset[r].add(current)
                    colset[c].add(current)
                    gridset[(r // 3, c // 3)].add(current)
        return True
