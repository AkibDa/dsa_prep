# Problem: Pacific Atlantic Water Flow

# Pattern: DFS from Borders.

# Why: Instead of checking if every cell can reach the ocean (hard), we start from the oceans and see which cells they can reach (easy). We find the intersection of cells reachable by both oceans.

def pacificAtlantic(heights):
  ROWS, COLS = len(heights), len(heights[0])
  pac, atl = set(), set()

  def dfs(r, c, visit, prevHeight):
    if ((r, c) in visit or r < 0 or c < 0 or
        r == ROWS or c == COLS or heights[r][c] < prevHeight):
      return
    visit.add((r, c))
    dfs(r + 1, c, visit, heights[r][c])
    dfs(r - 1, c, visit, heights[r][c])
    dfs(r, c + 1, visit, heights[r][c])
    dfs(r, c - 1, visit, heights[r][c])

  for c in range(COLS):
    dfs(0, c, pac, heights[0][c])
    dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

  for r in range(ROWS):
    dfs(r, 0, pac, heights[r][0])
    dfs(r, COLS - 1, atl, heights[r][COLS - 1])

  return list(pac.intersection(atl))

# Complexity: Time O(MxN) | Space O(MxN)