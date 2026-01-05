# Problem: Sudoku Solver

# Pattern: Backtracking (Matrix).

# Why: Find an empty cell. Try digits 1-9. If a digit is valid (check row, col, 3x3 box), place it and recurse. If recursion returns False, reset cell to empty and try next digit.

def solveSudoku(board):
  def isValid(r, c, k):
    for i in range(9):
      if board[r][i] == k: return False
      if board[i][c] == k: return False
      if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == k:
        return False
    return True

  def solve():
    for r in range(9):
      for c in range(9):
        if board[r][c] == ".":
          for k in "123456789":
            if isValid(r, c, k):
              board[r][c] = k
              if solve(): return True
              board[r][c] = "."
          return False
    return True

  solve()

# Complexity: Time O(9^M) (M is number of empty cells) | Space O(1)