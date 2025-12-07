from collections import deque

class Solution:
  def sortedSquares(self, nums: list[int]) -> list[int]:
    ans = deque()
    left, right = 0, len(nums) - 1
    while left <= right:
      if abs(nums[left]) > abs(nums[right]):
        ans.appendleft(nums[left] ** 2)
        left += 1
      else:
        ans.appendleft(nums[right] ** 2)
        right -= 1
    return list(ans)

# Example usage:
sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))