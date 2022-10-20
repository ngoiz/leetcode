class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        expected = set(range(n+1))
        for i in range(n):
            expected.remove(nums[i])
        
        return expected.pop()