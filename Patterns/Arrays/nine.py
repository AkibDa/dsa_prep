# Problem: Rotate Array

# Pattern: Reversal Algorithm.

# Why: Rotating k steps is equivalent to reversing the whole array, then reversing the first $k$ elements, then the rest.

def rotate(nums, k):
  k = k % len(nums)
  l, r = 0, len(nums) - 1
  while l < r:  # Reverse Logic
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l + 1, r - 1

  l, r = 0, k - 1
  while l < r:  # Reverse first k
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l + 1, r - 1

  l, r = k, len(nums) - 1
  while l < r:  # Reverse rest
    nums[l], nums[r] = nums[r], nums[l]
    l, r = l + 1, r - 1

# Complexity: Time O(N) | Space O(1)