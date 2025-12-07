class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    triplets = []
    nums.sort()

    for indx, val in enumerate(nums):
      if indx > 0 and val == nums[indx - 1]:
        continue

      left, right = indx + 1, len(nums) - 1

      while left < right:
        current_sum = val + nums[left] + nums[right]

        if current_sum < 0:
          left += 1
        elif current_sum > 0:
          right -= 1
        else:
          triplets.append([val, nums[left], nums[right]])

          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

    return triplets

# Example usage:
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))