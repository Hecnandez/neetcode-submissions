class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                square = board[row][col]
                if square == ".":
                    continue
                if (square in rows[row] or 
                    square in cols[col] or 
                    square in squares[(row//3, col//3)]):
                    return False
                cols[col].add(square)
                rows[row].add(square)
                squares[(row//3, col//3)].add(square)
        return True