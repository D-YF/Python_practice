from typing import List, Optional

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        path = []

        def isValid(row, column, path, n):
            column_left, column_right = column-1, column+1
            row_left, row_right = row-1, row-1
            
            for i in range(row):
                if path[i][column]=="Q":
                    return False
            
            while column_left>=0 and row_left>=0:
                if path[row_left][column_left]=="Q":
                    return False
                column_left -= 1
                row_left -= 1
            
            while column_right<n and row_right>=0:
                if path[row_right][column_right]=="Q":
                    return False
                column_right += 1
                row_right -= 1
            
            return True

        def traceback(n):
            if len(path)==n:
                ans.append(path[:])
                return
            
            for i in range(n):
                if isValid(len(path), i, path, n):
                    layer = "."*i + "Q" + "."*(n-i-1)
                    path.append(layer)
                    traceback(n)
                    path.pop()
                else:
                    continue

            return
        
        traceback(n)
        return ans


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.traceback(board)

    def isValid(self, row, col, k, board):
        
        for i in range(len(board)):
            if board[i][col] == k:
                return False
        
        for j in range(len(board[row])):
            if board[row][j] == k:
                return False

        start_row, start_col = (row//3)*3, (col//3)*3
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j]==k:
                    return False

        return True

        
    def traceback(self, board) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    continue
                
                for i in range(1,10):
                    k = str(i)
                    if self.isValid(row, col, k, board):
                        board[row][col] = k
                        if self.traceback(board):
                            return True
                        board[row][col] = '.'
                # 1-9 is invalid, return false
                return False
        # find solution
        return True
        