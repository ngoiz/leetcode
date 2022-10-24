class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        appearing_once = set()
        appearing_twice = set()        
        for num in nums:
            if num in appearing_twice:
                continue  
            elif num in appearing_once:
                appearing_once.remove(num)
                appearing_twice.add(num)
            else:
                appearing_once.add(num)
        
        if len(appearing_once) == 0:
            return -1
        else:
            return max(appearing_once)
        
            