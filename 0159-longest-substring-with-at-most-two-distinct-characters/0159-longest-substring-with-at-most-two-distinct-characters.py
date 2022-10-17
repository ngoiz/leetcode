class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        letters = set()
        
        for right in range(len(s)):

            letters.add(s[right])

            if len(letters) > 2:
                left += 1
                letters = set(s[left:right+1])

        max_w = right - left + 1
            
        return max_w
            