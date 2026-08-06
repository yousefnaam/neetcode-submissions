class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row: 1-9 no duplicates
        col: 1-9 no duplicates
        subboxes: 1-9 no duplicates
        use a set for each row, col, and subbox
        
        """
        rowset = [set() for _ in range(len(board))]
        colset = [set() for _ in range(len(board[0]))]
        subset = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rowset[row] or board[row][col] in colset[col] or board[row][col] in subset[(row//3,col//3)]:
                    return False
                rowset[row].add(board[row][col])
                colset[col].add(board[row][col])
                subset[(row//3,col//3)].add(board[row][col])
        return True


