class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and stk[-1][1] < temperatures[i]:
                stk_i, stk_temp = stk.pop()
                ans[stk_i] = i - stk_i
            
            stk.append((i, temperatures[i]))
        return ans
        