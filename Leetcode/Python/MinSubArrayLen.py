class Solution:
  def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    l = 0
    total = 0
    res = float("inf")
    for r in range(len(nums)):
      total += nums[r]
      while total >= target:
        res = min(res, r - l + 1)
        total -= nums[l]
        l += 1
    return res if res != float("inf") else 0

# Example usage:
sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(4, [1,4,4]))