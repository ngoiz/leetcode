class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {'b': 1,
                      'a': 1,
                      'l': 2,
                      'o': 2,
                      'n': 1}
        
        balloon_letters = set(balloon_dict.keys())
        
        curr_dict = {'b': 0,
                      'a': 0,
                      'l': 0,
                      'o': 0,
                      'n': 0}
        
        ans = 0
        for letter in text:
            if letter in balloon_letters:
                curr_dict[letter] += 1
        
        # At most can spell out the mod
        for letter in curr_dict.keys():
            curr_dict[letter] = curr_dict[letter] // balloon_dict[letter] 

        ans = min(curr_dict.values())
                    
        return ans