# Problem: Unique Paths

# Pattern: 2D DP (Grid).

# Why: To reach cell (r, c), you must have come from (r+1, c) or (r, c+1). We sum the ways from those two cells.

def uniquePaths(m, n):
  row = [1] * n

  for i in range(m - 1):
    newRow = [1] * n
    for j in range(n - 2, -1, -1):
      newRow[j] = newRow[j + 1] + row[j]
    row = newRow

  return row[0]

# Complexity: Time O(MxN) | Space O(N) (Row optimization)