class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        curr = 1

        for _ in range(2, n+1):
            prev, curr = curr, prev + curr

        return curr