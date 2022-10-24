from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        losses = defaultdict(int)
        played = set()
        
        for game in matches:
            played.add(game[0])
            played.add(game[1])
            losses[game[1]] += 1
            
        ans = [[], []]
        for player in sorted(played):
            if player not in losses:
                ans[0].append(player)
            elif losses[player] == 1:
                ans[1].append(player)
                
        return ans