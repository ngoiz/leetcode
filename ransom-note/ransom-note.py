from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = defaultdict(int)
        for letter in magazine:
            available_letters[letter] += 1
            
        for letter in ransomNote:
            if available_letters[letter] == 0:
                return False
            else:
                available_letters[letter] -= 1
                
        return True