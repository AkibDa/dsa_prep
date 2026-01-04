# Problem: Next Greater Element I

# Pattern: Monotonic Stack (Decreasing).

# Why: To find the next greater element efficiently, we keep a stack of elements that haven't found a greater element yet. When we see a number n greater than stack.top(), n is the "next greater" for stack.top().

def nextGreaterElement(nums1, nums2):
  res = {}  # Map val -> next greater
  stack = []

  for n in nums2:
    while stack and n > stack[-1]:
      res[stack.pop()] = n
    stack.append(n)

  return [res.get(n, -1) for n in nums1]

# Complexity: Time O(N+M) | Space O(N)