# Problem: Implement strStr()

# Pattern: Sliding Window (Fixed Size).

# Why: We check every substring of length needle against the needle. (KMP is efficient but overkill for general interviews unless asked).

def strStr(haystack, needle):
  if needle == "":
    return 0

  for i in range(len(haystack) + 1 - len(needle)):
    if haystack[i: i + len(needle)] == needle:
      return i
  return -1

# Complexity: Time O(NxM) | Space O(1)