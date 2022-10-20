class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        # could do import string; alphabet = set(string.ascii_lowercase)
        
        set_sentence = set(sentence)
        
        difference = alphabet - set_sentence
        
        if len(difference) == 0:
            return True
        else:
            return False