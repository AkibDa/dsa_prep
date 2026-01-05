# Problem: Coin Change

# Pattern: Unbounded Knapsack (Bottom-Up).

# Why: We want the minimum coins for amount a. We check every coin c: dp[a] = 1 + dp[a - c]. It's "unbounded" because we can use the same coin multiple times.

def coinChange(coins, amount):
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0

  for a in range(1, amount + 1):
    for c in coins:
      if a - c >= 0:
        dp[a] = min(dp[a], 1 + dp[a - c])

  return dp[amount] if dp[amount] != float('inf') else -1

# Complexity: Time O(AxC) (Amount * Coins) | Space O(A)