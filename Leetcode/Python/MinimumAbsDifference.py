class Solution:
  def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
    result = []
    sort_arr = sorted(arr)
    minimum = sort_arr[1] - sort_arr[0]

    for i in range(len(sort_arr) - 1):
      sub = sort_arr[i + 1] - sort_arr[i]
      if sub < minimum:
        minimum = sub
        result = [[sort_arr[i], sort_arr[i + 1]]]
      elif sub == minimum:
        result.append([sort_arr[i], sort_arr[i + 1]])

    return result

# Example usage:
sol = Solution()
print(sol.minimumAbsDifference([4,2,1,3]))