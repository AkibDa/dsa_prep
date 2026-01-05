# Problem: Rotting Oranges

# Pattern: Multi-Source BFS.

# Why: The rot spreads layer by layer from all rotten oranges simultaneously. BFS is perfect for "shortest time" or "level-by-level" spreading.

import collections


def orangesRotting(grid):
  q = collections.deque()
  time, fresh = 0, 0
  ROWS, COLS = len(grid), len(grid[0])

  for r in range(ROWS):
    for c in range(COLS):
      if grid[r][c] == 1: fresh += 1
      if grid[r][c] == 2: q.append((r, c))

  directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  while q and fresh > 0:
    for i in range(len(q)):
      r, c = q.popleft()
      for dr, dc in directions:
        row, col = r + dr, c + dc
        if (row < 0 or row == ROWS or col < 0 or
            col == COLS or grid[row][col] != 1):
          continue
        grid[row][col] = 2
        q.append((row, col))
        fresh -= 1
    time += 1
  return time if fresh == 0 else -1

# Complexity: Time O(MxN) | Space O(MxN)