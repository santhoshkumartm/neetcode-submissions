class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)

        # check 3x3 cells
        for rowStart in [0, 3, 6]:
            for colStart in [0, 3, 6]:
                seen = set()
                for r in range(rowStart, rowStart + 3):
                    for c in range(colStart, colStart + 3):
                        val = board[r][c]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True
