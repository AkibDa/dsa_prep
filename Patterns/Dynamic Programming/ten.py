# Problem: Partition Equal Subset Sum

# Pattern: 0/1 Knapsack.

# Why: If we can partition the array into two equal subsets, the sum of each subset must be totalSum / 2. We just need to find if any subset sums to exactly target = totalSum / 2.

def canPartition(nums):
  if sum(nums) % 2:
    return False

  dp = set()
  dp.add(0)
  target = sum(nums) // 2

  for i in range(len(nums) - 1, -1, -1):
    nextDP = set()
    for t in dp:
      if (t + nums[i]) == target:
        return True
      nextDP.add(t + nums[i])
      nextDP.add(t)
    dp = nextDP

  return True if target in dp else False

# Complexity: Time O(NxSum) | Space O(Sum)