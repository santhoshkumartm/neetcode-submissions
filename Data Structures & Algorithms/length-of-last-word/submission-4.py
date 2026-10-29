class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # le=0
        # for ch in s.split(' '):
        #     if len(ch)!=0:
        #         le=len(ch) 
        # return le

        length,i=0,len(s)-1

        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length