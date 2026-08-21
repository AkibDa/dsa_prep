class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        
        for i in range(1, 1 << n):
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = math.lcm(curr_lcm, coins[j])
                    bits += 1
            subsets.append((curr_lcm, 1 if bits % 2 == 1 else -1))
            
        def count_multiples(x: int) -> int:
            return sum(sign * (x // l) for l, sign in subsets)

        left = 1
        right = min(coins) * k
        
        while left < right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                right = mid
            else:
                left = mid + 1
                
        return left