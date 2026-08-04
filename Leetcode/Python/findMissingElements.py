class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        smallest = min(nums)
        largest = max(nums)

        for i in range(smallest, largest, 1):
            if i in nums:
                continue
            else:
                res.append(i)
        
        return res
        