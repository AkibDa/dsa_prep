# Problem: Product of Array Except Self

# Pattern: Prefix & Suffix Products.

# Why: Division is forbidden. We calculate the product of everything to the left, then multiply by the product of everything to the right.

def productExceptSelf(nums):
  res = [1] * len(nums)

  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

  postfix = 1
  for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]

  return res

# Complexity: Time O(N) | Space O(1) (ignoring output array)