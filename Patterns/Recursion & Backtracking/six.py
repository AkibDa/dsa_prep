# Problem: N-Queens

# Pattern: Backtracking (Constraint Propagation).

# Why: We place a queen row by row. We maintain Sets to track occupied columns, positive diagonals, and negative diagonals to validate moves in O(1).

def solveNQueens(n):
  col = set()
  posDiag = set()  # (r + c)
  negDiag = set()  # (r - c)
  res = []
  board = [["."] * n for _ in range(n)]

  def backtrack(r):
    if r == n:
      res.append(["".join(row) for row in board])
      return

    for c in range(n):
      if c in col or (r + c) in posDiag or (r - c) in negDiag:
        continue

      col.add(c)
      posDiag.add(r + c)
      negDiag.add(r - c)
      board[r][c] = "Q"

      backtrack(r + 1)

      col.remove(c)
      posDiag.remove(r + c)
      negDiag.remove(r - c)
      board[r][c] = "."

  backtrack(0)
  return res

# Complexity: Time O(N!) | Space O(N^2)