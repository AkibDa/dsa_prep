# Problem: Maximum Product Subarray

# Pattern: DP with State Tracking (Min & Max).

# Why: A negative number can flip the smallest product into the largest product. Therefore, we must track both the curMax and curMin at every step.

def maxProduct(nums):
  res = max(nums)
  curMin, curMax = 1, 1

  for n in nums:
    if n == 0:
      curMin, curMax = 1, 1
      continue

    tmp = curMax * n
    curMax = max(n * curMax, n * curMin, n)
    curMin = min(tmp, n * curMin, n)
    res = max(res, curMax)

  return res

# Complexity: Time O(N) | Space O(1)