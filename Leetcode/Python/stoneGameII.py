class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sums = [0] * n
        suffix_sums[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i: int, M: int) -> int:
            if i >= n:
                return 0
                
            if i + 2 * M >= n:
                return suffix_sums[i]
                
            if (i, M) in memo:
                return memo[(i, M)]
                
            res = 0
            for x in range(1, 2 * M + 1):
                res = max(res, suffix_sums[i] - dfs(i + x, max(M, x)))
                
            memo[(i, M)] = res
            return res
            
        return dfs(0, 1)