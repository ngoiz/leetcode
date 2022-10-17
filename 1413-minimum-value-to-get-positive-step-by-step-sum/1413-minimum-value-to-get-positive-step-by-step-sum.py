class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
            
        start_value = max(1 - nums[0], 1)
            
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
    
            if prefix[-1] + start_value < 1:
                start_value += 1 - (prefix[-1] + start_value)
        
        return start_value