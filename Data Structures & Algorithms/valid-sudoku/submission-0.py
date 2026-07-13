from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                if d in rows[r] or d in cols[c] or d in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(d)
                cols[c].add(d)
                boxes[(r // 3, c // 3)].add(d)

        return True