class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        r=0
        l=len(cleaned)-1
        # print(s[r],s[l])

        while r<l:
            print(cleaned[r],cleaned[l])
            if cleaned[r]==cleaned[l]:
                
                r+=1
                l-=1
            else:
                return False
        return True
