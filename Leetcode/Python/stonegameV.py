from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        m = [i - 1 for i in range(n)]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                while m[i] + 1 < j and (prefix[m[i] + 2] - prefix[i]) * 2 <= prefix[j + 1] - prefix[i]:
                    m[i] += 1
                    
                M = m[i]
                ans = 0
                
                if M >= i:
                    if (prefix[M + 1] - prefix[i]) * 2 == prefix[j + 1] - prefix[i]:
                        ans = max(max_l[i][M], max_r[M + 1][j])
                    else:
                        ans = max_l[i][M]
                        if M + 2 <= j:
                            ans = max(ans, max_r[M + 2][j])
                else:
                    ans = max_r[i + 1][j]
                    
                dp[i][j] = ans
                
                sum_ij = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], ans + sum_ij)
                max_r[i][j] = max(max_r[i + 1][j], ans + sum_ij)
                
        return dp[0][n - 1]