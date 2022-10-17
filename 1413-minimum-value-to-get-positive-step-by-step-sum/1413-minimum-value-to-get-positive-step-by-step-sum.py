class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
            
        start_value = max(1 - nums[0], 1)
            
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
            diff = prefix[-1] + start_value
            if diff < 1:
                start_value += 1 - diff
        
        return start_value