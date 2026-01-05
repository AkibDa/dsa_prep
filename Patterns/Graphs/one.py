# Problem: Number of Islands

# Pattern: DFS / BFS (Grid Traversal).

# Why: We iterate through every cell. If we find a "1" (land), it initiates a new island. We then run DFS/BFS to "sink" (mark as visited) all connected land so we don't count it again.

def numIslands(grid):
  if not grid: return 0
  rows, cols = len(grid), len(grid[0])
  islands = 0

  def dfs(r, c):
    if (r < 0 or c < 0 or r >= rows or
        c >= cols or grid[r][c] == "0"):
      return

    grid[r][c] = "0"  # Mark as visited (sink it)
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == "1":
        dfs(r, c)
        islands += 1
  return islands

# Complexity: Time O(MxN) | Space O(MxN) (recursion stack)