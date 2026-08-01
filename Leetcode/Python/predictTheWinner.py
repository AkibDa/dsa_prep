class Solution:
  def predictTheWinner(self, nums: List[int]) -> bool:
    n = len(nums)
    dp = nums[:]

    for length in range(2, n + 1):
      for i in range(n - length + 1):
        j = i + length - 1

        pick_left = nums[i] - dp[i + 1]
        pick_right = nums[j] - dp[i]

        dp[i] = max(pick_left, pick_right)

    return dp[0] >= 0
