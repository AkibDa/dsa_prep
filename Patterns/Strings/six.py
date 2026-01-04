# Problem: Reverse Words in a String

# Pattern: Two Pointers (or Built-in Split/Join).

# Why: We need to handle multiple spaces. In Python, split() without arguments automatically handles multiple spaces and trims.

def reverseWords(s):
  # Split by whitespace and filter out empty strings
  words = s.split()
  # Reverse the list of words
  words.reverse()
  # Join them back with a single space
  return " ".join(words)

# Complexity: Time O(N) | Space O(N)