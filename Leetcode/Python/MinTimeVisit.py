class Solution:
  def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
    res = 0
    x1, y1 = points.pop()
    while points:
      x2, y2 = points.pop()
      res += max(abs(x2 - x1), abs(y2 - y1))
      x1, y1 = x2, y2
    return res

# Example usage:
sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))
print(sol.minTimeToVisitAllPoints([[0,0],[1,1],[1,2]]))