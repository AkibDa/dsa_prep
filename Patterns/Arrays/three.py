# Problem: Maximum Subarray (Kadane’s Algorithm)

# Pattern: Dynamic Programming (Kadane's).

# Why: We carry the subarray sum forward. If the current running sum becomes negative, it contributes nothing to future subarrays, so we reset it to 0.

def maxSubArray(nums):
  max_sub = nums[0]
  cur_sum = 0

  for n in nums:
    if cur_sum < 0:
      cur_sum = 0
    cur_sum += n
    max_sub = max(max_sub, cur_sum)
  return max_sub

# Complexity: Time O(N) | Space O(1)