# Problem: Word Break

# Pattern: 1D DP (Boolean Check).

# Why: dp[i] is True if the substring s[0:i] can be broken into valid words. We check every partition j < i. If dp[j] is True AND s[j:i] is in the dictionary, then dp[i] is True.

def wordBreak(s, wordDict):
  dp = [False] * (len(s) + 1)
  dp[len(s)] = True

  for i in range(len(s) - 1, -1, -1):
    for w in wordDict:
      if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
        dp[i] = dp[i + len(w)]
      if dp[i]:
        break

  return dp[0]

# Complexity: Time O(NxMxL) (N=len(s), M=dicts size, L=avg word len) | Space O(N)