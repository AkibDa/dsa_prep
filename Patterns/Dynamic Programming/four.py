# Problem: Longest Increasing Subsequence

# Pattern: 1D DP (Nested Loop).

# Why: For every number i, look back at all previous numbers j. If nums[i] > nums[j], then i can extend the subsequence ending at j.

def lengthOfLIS(nums):
  LIS = [1] * len(nums)

  for i in range(len(nums) - 1, -1, -1):
    for j in range(i + 1, len(nums)):
      if nums[i] < nums[j]:
        LIS[i] = max(LIS[i], 1 + LIS[j])

  return max(LIS)

# Complexity: Time O(N^2) | Space O(N) (Note: Can be improved to O(N log N) using Binary Search/Patience Sorting).