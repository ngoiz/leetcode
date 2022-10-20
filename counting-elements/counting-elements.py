class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        target_set = set(arr)  # O(n)
        
        count = 0
        for elem in arr:
            if (elem + 1) in target_set:  
                count += 1
        return count