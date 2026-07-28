class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row unique check
        for row in board:
            row_set = set()
            for element in row:
                if element == ".":
                    continue
                if element in row_set:
                    return False
                row_set.add(element)

        # col unique check
        col_len = len(board[0])
        for col in range(col_len):
            col_set = set()
            for row in board:
                element = row[col]
                if element == ".":
                    continue
                if element in col_set:
                    return False
                col_set.add(element)

        # 3 x 3 box check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        element = board[row][col]
                        if element == ".":
                            continue
                        if element in box_set:
                            return False
                        box_set.add(element)
        return True