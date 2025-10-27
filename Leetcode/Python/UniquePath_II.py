class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1:
      return 0

    dp = [0] * n

    dp[0] = 1

    for j in range(1,n):
      dp[j] = 1 if obstacleGrid[0][j] == 0 and dp[j-1] == 1 else 0

    for i in range(1, m):
      if obstacleGrid[i][0] == 1:
        dp[0] = 0
      for j in range(1, n):
        if obstacleGrid[i][j] == 1:
          dp[j] = 0
        else:
          dp[j] = dp[j] + dp[j-1]


    return dp[n-1]