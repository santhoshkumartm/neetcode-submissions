class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        le=0
        for ch in s.split(' '):
            if len(ch)!=0:
                le=len(ch) 
        return le