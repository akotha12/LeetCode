class Solution(object):
    def isValidSudoku(self, board):
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range (9):
                if not board[i][j] == ".":
                    if (board[i][j] in cols[i] or board[i][j] in rows[j] or board[i][j] in squares[(i // 3, j // 3)]):
                        return False
                    cols[i].add(board[i][j])
                    rows[j].add(board[i][j])
                    squares[(i // 3, j // 3)].add(board[i][j])
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        