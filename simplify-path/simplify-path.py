class Solution:
    def simplifyPath(self, path: str) -> str:
        simple_path = []
        
        actions = path.split('/')
        
        for action in actions:
            if not action:
                continue
            if action == '..':
                if simple_path:
                    simple_path.pop()
            elif action == '.':
                continue
            else:
                simple_path.append(action)
        
        return '/' + '/'.join(simple_path)