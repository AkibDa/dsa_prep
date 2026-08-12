def maxSubarrayLength(nums: list[int], k: int) -> int:
    freq = {}
    max_len = 0
    left = 0
    
    for right in range(len(nums)):
        current_num = nums[right]
        freq[current_num] = freq.get(current_num, 0) + 1
        
        while freq[current_num] > k:
            freq[nums[left]] -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len