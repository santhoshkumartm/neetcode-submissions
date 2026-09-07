class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack=[]
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in bracket_map:
                if not stack:
                    return False
                top=stack.pop()
                if top!=bracket_map[c]:
                    return False
            else:
                stack.append(c)
        return not stack