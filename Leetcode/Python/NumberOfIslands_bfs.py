from collections import deque

class Solution:
  def numIslands(self, grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0

    def bfs(i, j):
      queue = deque([(i, j)])
      grid[i][j] = "0"

      while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nx, ny = x + dx, y + dy
          if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
            grid[nx][ny] = "0"
            queue.append((nx, ny))

    for i in range(m):
      for j in range(n):
        if grid[i][j] == "1":
          count += 1
          bfs(i, j)

    return count

# Example usage:
sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
