class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m = n
        s = 0
        p = 1

        while m > 0:
            digit = m % 10
            s = s + digit
            p = p * digit
            m = m // 10

        if n % (s + p) == 0:
            return True
        else:
            return False
        