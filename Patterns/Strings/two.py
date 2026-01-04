# Problem: Valid Anagram

# Pattern: Hash Map (Frequency Count).

# Why: Anagrams must have the exact same characters with the exact same counts. We map character -> count.

def isAnagram(s, t):
  if len(s) != len(t):
    return False

  countS, countT = {}, {}

  for i in range(len(s)):
    countS[s[i]] = countS.get(s[i], 0) + 1
    countT[t[i]] = countT.get(t[i], 0) + 1

  return countS == countT

# Complexity: Time O(N) | Space O(1) (since there are at most 26 lowercase English letters).