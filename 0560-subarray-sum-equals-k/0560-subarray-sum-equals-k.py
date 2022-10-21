from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Initialise hashmap
        counts = defaultdict(int)  # int: int maps the prefix sum with the frequency of that sum
        counts[0] = 1
        
        ans = 0
        curr = 0  # prefix sum
        
        for number in nums:
            curr += number  # update prefix
            
            ans += counts[curr-k] # number of subarrays finishing at current index that satisfy conts. Else it deaults to 0
            counts[curr] += 1  # update prefix frequency
        
        return ans