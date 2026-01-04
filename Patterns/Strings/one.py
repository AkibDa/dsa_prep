# Problem: Longest Substring Without Repeating Characters

# Pattern: Sliding Window (Variable Size).

# Why: We need to find the longest continuous slice. We expand the window (right pointer) and contract it from the left whenever a duplicate character is found.

def lengthOfLongestSubstring(s):
  charSet = set()
  l = 0
  res = 0

  for r in range(len(s)):
    while s[r] in charSet:
      charSet.remove(s[l])
      l += 1
    charSet.add(s[r])
    res = max(res, r - l + 1)
  return res

# Complexity: Time O(N) | Space O(N) (for the Set)