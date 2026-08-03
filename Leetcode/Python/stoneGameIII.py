class Solution:
  def stoneGameIII(self, stoneValue: List[int]) -> str:
    n = len(stoneValue)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      res = float("-inf")
      current_sum = 0
      for k in range(3):
        if i + k < n:
          current_sum += stoneValue[i + k]
          res = max(res, current_sum - dp[i + k + 1])
        else:
          break
      dp[i] = res

    if dp[0] > 0:
      return "Alice"
    elif dp[0] < 0:
      return "Bob"
    else:
      return "Tie"