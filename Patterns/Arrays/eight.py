# Problem: Set Matrix Zeroes

# Pattern: In-place Hashing (Using array as storage).

# Why: We need O(1) space. Instead of a separate visited array, use the first row and first column to flag if a row/col should be zeroed.

def setZeroes(matrix):
  ROWS, COLS = len(matrix), len(matrix[0])
  rowZero = False  # Extra variable for the first row specifically

  for r in range(ROWS):
    for c in range(COLS):
      if matrix[r][c] == 0:
        matrix[0][c] = 0
        if r > 0:
          matrix[r][0] = 0
        else:
          rowZero = True

  for r in range(1, ROWS):
    for c in range(1, COLS):
      if matrix[0][c] == 0 or matrix[r][0] == 0:
        matrix[r][c] = 0

  if matrix[0][0] == 0:
    for r in range(ROWS): matrix[r][0] = 0
  if rowZero:
    for c in range(COLS): matrix[0][c] = 0

# Complexity: Time O(MxN) | Space O(1)