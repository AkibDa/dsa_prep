# Problem: Climbing Stairs

# Pattern: 1D DP (Fibonacci Sequence).

# Why: To reach step n, you could have come from step n-1 or n-2. Thus, ways(n) = ways(n-1) + ways(n-2).

def climbStairs(n):
  one, two = 1, 1

  for i in range(n - 1):
    temp = one
    one = one + two
    two = temp

  return one

# Complexity: Time O(N) | Space O(1)