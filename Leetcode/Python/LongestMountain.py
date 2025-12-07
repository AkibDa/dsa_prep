class Solution:
  def longestMountain(self, arr: list[int]) -> int:
    rest = 0
    for i in range(1,len(arr) - 1):
      if arr[i-1] < arr[i] > arr[i+1]:
        l, r = i, i
        while l > 0 and arr[l-1] < arr[l]:
          l -= 1
        while r < len(arr) - 1 and arr[r] > arr[r+1]:
          r += 1
        rest = max(rest, r - l + 1)
    return rest

# Example usage:
sol = Solution()
print(sol.longestMountain([2,1,4,7,3,2,5]))
print(sol.longestMountain([2,2,2]))