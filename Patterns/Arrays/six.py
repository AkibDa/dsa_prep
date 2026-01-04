# Problem: 3Sum

# Pattern: Two Pointers (with Sorting).

# Why: Finding three numbers is hard, but if we fix one number, it becomes a "Two Sum" problem (finding two numbers that add up to -target). Sorting allows us to avoid duplicates and use two pointers.

def threeSum(nums):
  res = []
  nums.sort()

  for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:  # Skip duplicates
      continue

    l, r = i + 1, len(nums) - 1
    while l < r:
      threeSum = a + nums[l] + nums[r]
      if threeSum > 0:
        r -= 1
      elif threeSum < 0:
        l += 1
      else:
        res.append([a, nums[l], nums[r]])
        l += 1
        while nums[l] == nums[l - 1] and l < r:
          l += 1
  return res

# Complexity: Time O(N^2) | Space O(1) or O(N) depending on sort implementation.