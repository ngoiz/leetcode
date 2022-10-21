from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        curr = 0
        counts = defaultdict(int)
        counts[0] = -1
        max_w = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            # print('Running sum', curr)
            # print('Dict', counts)
            
            if curr in counts:
                ws = i - counts[curr]
                max_w = max(max_w, ws)
                # print('Len', ws)
                # print('Max Window size', max_w)
            else:
                counts[curr] = i

        return max_w