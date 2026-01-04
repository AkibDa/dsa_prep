# Problem: Daily Temperatures

# Pattern: Monotonic Stack (storing indices).

# Why: We need to find the distance to the next warmer day. We store indices in the stack. When we find a warmer temperature, we pop the previous index and calculate current_index - popped_index.

def dailyTemperatures(temperatures):
  res = [0] * len(temperatures)
  stack = []  # pair: [temp, index]

  for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
      stackT, stackInd = stack.pop()
      res[stackInd] = i - stackInd
    stack.append([t, i])

  return res

# Complexity: Time O(N) | Space O(N)