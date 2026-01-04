# Problem: Missing Number

# Pattern: Cyclic Sort / Math.

# Why: The numbers are in range [0, n]. The sum of [0...n] is a known math formula (n(n+1)/2). Subtract the actual sum to find the missing piece.

def missingNumber(nums):
  res = len(nums)
  for i in range(len(nums)):
    res += (i - nums[i])
  return res
  # Alternative: return sum(range(len(nums)+1)) - sum(nums)

# Complexity: Time O(N) | Space O(1)