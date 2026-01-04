# Problem: Longest Palindromic Substring

# Pattern: Expand Around Center.

# Why: A palindrome mirrors around its center. For every character, treat it as the center and expand outwards to see how long the palindrome is. Note: You must handle both odd centers (aba) and even centers (abba).

def longestPalindrome(s):
  res = ""

  for i in range(len(s)):
    # Odd length palindrome
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
      if (r - l + 1) > len(res):
        res = s[l:r + 1]
      l -= 1
      r += 1

    # Even length palindrome
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      if (r - l + 1) > len(res):
        res = s[l:r + 1]
      l -= 1
      r += 1

  return res

# Complexity: Time O(N^2) | Space O(1)