from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.locations = defaultdict(list)
        
        for idx, word in enumerate(wordsDict): # runs once O(n)
            self.locations[word].append(idx)
        
        self.length = len(wordsDict)
        
    def shortest(self, word1: str, word2: str) -> int:
        
        min_distance = self.length
        
        locs1 = self.locations[word1]
        locs2 = self.locations[word2]

        for i in locs1:
            for j in locs2:
                min_distance = min(min_distance, abs(i-j))
                
        return min_distance
        
        

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)