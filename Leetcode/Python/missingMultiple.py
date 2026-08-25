class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)

        i = 1
        while True:

            multiple = i * k

            if multiple not in num_set:
                return multiple
                
            i += 1