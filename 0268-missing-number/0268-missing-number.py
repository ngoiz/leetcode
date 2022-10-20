class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Missing number is the difference between expected sum to n and sum of nums"""
        n = len(nums)
        
        running_sum = 0
        expected_sum = n  # initialise here since range is [0, n]
        for i in range(n):
            running_sum += nums[i]
            expected_sum += i
            
        return expected_sum - running_sum