class Solution:
    def makeGood(self, s: str) -> str:
        good_string = []
        
        for letter in s:
            if good_string:
                if letter.isupper() and good_string[-1] == letter.lower():
                    good_string.pop()
                    continue
                elif letter == good_string[-1].lower() and good_string[-1].isupper():
                    good_string.pop()
                    continue
            good_string.append(letter)
        return ''.join(good_string)