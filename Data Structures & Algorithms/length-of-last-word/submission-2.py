class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # le=0
        # for ch in s.split(' '):
        #     if len(ch)!=0:
        #         le=len(ch) 
        # return le

        i = len(s) - 1
        # Step 1: skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        # Step 2: count characters of last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length