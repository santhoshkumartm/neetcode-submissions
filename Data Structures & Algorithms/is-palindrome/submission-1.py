class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        # r=0
        # l=len(cleaned)-1

        # while r<l:
        #     print(cleaned[r],cleaned[l])
        #     if cleaned[r]==cleaned[l]:
                
        #         r+=1
        #         l-=1
        #     else:
        #         return False
        # return True
        newstr=''

        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        return newstr==newstr[::-1]
        print(newstr)