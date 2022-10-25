class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        
        min_length = min(len1, len2)
        
        ans = []
        for i in range(min_length):
            ans.extend([word1[i], word2[i]])
            
        if len1 < len2:
            ans.append(word2[i+1:])
        elif len1 > len2:
            ans.append(word1[i+1:])
        
        return ''.join(ans)