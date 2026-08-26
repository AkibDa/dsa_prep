class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        
        count = left = 0
        ans = s

        for right, ch in enumerate(s):
            count += int(ch)
            while count > k or s[left] == "0":
                count -= int(s[left])
                left+= 1
            if count == k:
                st = s[left:right+1]
                if len(st) < len(ans) or len(st) == len(ans) and st < ans:
                    ans = st
        return ans