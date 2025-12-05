class Solution:
  def finalValueAfterOperations(self, operations: list[str]) -> int:
    value = 0
    for operation in operations:
      if "+" in operation:
        value += 1
      else:
        value -= 1
    return value

# Example usage:
sol = Solution()
print(sol.finalValueAfterOperations(["--X","X++","X++"]))
print(sol.finalValueAfterOperations(["++X","++X","X++"]))
print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))