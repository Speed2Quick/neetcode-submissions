class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        grids = {}

        cur_row = 0
        for row in board:
            for j, val in enumerate(row):
                if val == ".": continue

                if val in rows and rows[val] == cur_row:
                    return False
                elif val in columns and columns[val] == j:
                    return False
                elif val in grids and grids[val] == (cur_row // 3) * 3 + (j // 3):
                    return False

                rows[val] = cur_row
                columns[val] = j
                grids[val] = (cur_row // 3) * 3 + (j // 3)

            cur_row += 1

        return True
