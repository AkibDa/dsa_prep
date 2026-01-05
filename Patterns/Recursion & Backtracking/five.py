# Problem: Letter Combinations of a Phone Number

# Pattern: Backtracking (Multi-branch).

# Why: For each digit, we loop through its possible letters. If input is "23", at digit '2' we branch to 'a', 'b', 'c', and recursively solve for '3'.

def letterCombinations(digits):
  if not digits: return []
  res = []
  digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

  def backtrack(i, curStr):
    if len(curStr) == len(digits):
      res.append(curStr)
      return

    for c in digitToChar[digits[i]]:
      backtrack(i + 1, curStr + c)

  backtrack(0, "")
  return res

# Complexity: Time O(4^N) | Space O(N)