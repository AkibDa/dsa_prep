# Problem: Two Sum

# Pattern: Hash Map (Trade space for time).

# Why: We need to find a target value difference (target - current). Looking up a value in an array is O(N), but looking up in a Hash Map is O(1).

def twoSum(nums, target):
  prevMap = {}  # val : index

  for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i
  return []

# Complexity: Time O(N) | Space O(N)