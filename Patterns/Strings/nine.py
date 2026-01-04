# Problem: Decode Ways

# Pattern: Dynamic Programming (1D).

# Why: A decision at index i depends on i+1 (taking 1 digit) or i+2 (taking 2 digits). This creates overlapping subproblems.

def numDecodings(s):
  dp = {len(s): 1}

  for i in range(len(s) - 1, -1, -1):
    if s[i] == "0":
      dp[i] = 0
    else:
      dp[i] = dp[i + 1]

    if (i + 1 < len(s) and (s[i] == "1" or
                            (s[i] == "2" and s[i + 1] in "0123456"))):
      dp[i] += dp[i + 2]

  return dp[0]

# Complexity: Time O(N) | Space O(N)