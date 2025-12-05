class Solution:
  def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    hash = {}
    for i, num in enumerate(sorted(nums)):
      if num not in hash:
        hash[num] = i
    return [hash[num] for num in nums]

# Example usage:
sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
print(sol.smallerNumbersThanCurrent([6,5,4,8]))
print(sol.smallerNumbersThanCurrent([7,7,7,7]))