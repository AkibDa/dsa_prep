# Problem: Container With Most Water

# Pattern: Two Pointers (Greedy Shrinking).

# Why: Area is determined by the shorter line. To potentially find a larger area, we must move the pointer of the shorter line inward (hoping to find a taller line). Moving the taller line can never help.

def maxArea(height):
  l, r = 0, len(height) - 1
  res = 0

  while l < r:
    area = (r - l) * min(height[l], height[r])
    res = max(res, area)

    if height[l] < height[r]:
      l += 1
    else:
      r -= 1
  return res

# Complexity: Time O(N) | Space O(1)