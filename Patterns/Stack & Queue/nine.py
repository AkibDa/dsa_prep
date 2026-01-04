# Problem: Largest Rectangle in Histogram

# Pattern: Monotonic Stack (Increasing).

# Why: A bar can extend to the right/left as long as the bars are taller than it. When we see a smaller bar, we know the rectangle for the taller bars in the stack must end. We compute their areas then.

def largestRectangleArea(heights):
  maxArea = 0
  stack = []  # pair: (index, height)

  for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][1] > h:
      index, height = stack.pop()
      maxArea = max(maxArea, height * (i - index))
      start = index  # extend start index backwards
    stack.append((start, h))

  for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))

  return maxArea

# Complexity: Time O(N) | Space O(N)