class Solution:
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    res = []
    while matrix:
      res += matrix.pop(0)
      if matrix and matrix[0]:
        for row in matrix:
          res.append(row.pop())
      if matrix:
        res += matrix.pop()[::-1]
      if matrix and matrix[0]:
        for row in matrix[::-1]:
          res.append(row.pop(0))
    return res

# Example usage:
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(sol.spiralOrder([[1]]))