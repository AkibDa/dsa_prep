# Problem: Count and Say

# Pattern: Simulation / Iteration.

# Why: We must generate the sequence step-by-step. The output of step $n$ becomes the input for step n+1.

def countAndSay(n):
  if n == 1:
    return "1"

  prev = countAndSay(n - 1)
  res = ""
  count = 1

  for i in range(len(prev)):
    if i + 1 < len(prev) and prev[i] == prev[i + 1]:
      count += 1
    else:
      res += str(count) + prev[i]
      count = 1
  return res

# Complexity: Time O(2^N) (rough upper bound as string grows) | Space O(2^N)