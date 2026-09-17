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
        # newstr=''

        # for c in s:
        #     if c.isalnum():
        #         newstr+=c.lower()
        # return newstr==newstr[::-1]
        # print(newstr)



        # newstr=''
        # for c in s:
        #     if c.isalnum():
        #         newstr+=c.lower()
        # return newstr==newstr[::-1]

        l,r=0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            while s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
