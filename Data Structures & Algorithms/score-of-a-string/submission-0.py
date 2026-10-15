class Solution:
    def scoreOfString(self, s: str) -> int:
        result=0
        for i,ch in enumerate(s):
            if i+1 < len(s):
                result+=abs(ord(s[i])-ord(s[i+1]))
                # =val if val>=0 else -(val)
                print(result)
        return result