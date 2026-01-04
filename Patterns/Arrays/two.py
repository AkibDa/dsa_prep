# Problem: Best Time to Buy and Sell Stock

# Pattern: Sliding Window (Variable size) / Greedy.

# Why: We effectively expand our window as long as profit increases, but reset the "buy" pointer immediately if we find a lower price (greedy approach).

def maxProfit(prices):
  min_price = float('inf')
  max_profit = 0

  for price in prices:
    if price < min_price:
      min_price = price
    elif price - min_price > max_profit:
      max_profit = price - min_price

  return max_profit

# Complexity: Time O(N) | Space O(1)