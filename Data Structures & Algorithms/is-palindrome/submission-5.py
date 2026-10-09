class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return ""
        cleaned="".join(c.lower() for c in s if c.isalnum())
        print(cleaned)

        l=0
        r=len(cleaned)-1
        while l<r:
            print(s[l],s[r])
            if cleaned[l]!=cleaned[r]:
                return False
            l+=1
            r-=1
        return True