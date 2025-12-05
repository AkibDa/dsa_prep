class Solution:
  def finalValueAfterOperations(self, operations: list[str]) -> int:
    inr = "++"
    decr = "--"
    value = 0
    for operation in operations:
      if inr in operation:
        value += 1
      elif decr in operation:
        value -= 1
    return value

# Example usage:
sol = Solution()
print(sol.finalValueAfterOperations(["--X","X++","X++"]))
print(sol.finalValueAfterOperations(["++X","++X","X++"]))
print(sol.finalValueAfterOperations(["X++","++X","--X","X--"]))