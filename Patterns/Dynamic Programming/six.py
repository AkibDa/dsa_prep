# Problem: Edit Distance

# Pattern: 2D DP (String Alignment).

# Why: We compare word1[i] and word2[j].
#     If equal: No operation needed, look at i+1, j+1.
#     If distinct: We take the min of Insert, Delete, or Replace and add 1 operation cost.

def minDistance(word1, word2):
  dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

  for j in range(len(word2) + 1): dp[len(word1)][j] = len(word2) - j
  for i in range(len(word1) + 1): dp[i][len(word2)] = len(word1) - i

  for i in range(len(word1) - 1, -1, -1):
    for j in range(len(word2) - 1, -1, -1):
      if word1[i] == word2[j]:
        dp[i][j] = dp[i + 1][j + 1]
      else:
        dp[i][j] = 1 + min(dp[i + 1][j],  # Delete
                           dp[i][j + 1],  # Insert
                           dp[i + 1][j + 1])  # Replace
  return dp[0][0]

# Complexity: Time O(MxN) | Space O(MxN)