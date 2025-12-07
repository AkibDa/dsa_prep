class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0
    while r != len(prices):
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        max_profit = max(max_profit, profit)
      else:
        l = r
      r += 1
    return max_profit

# Example usage:
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))