class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return ""
        cleaned="".join(c.lower() for c in s if c.isalnum())
        l=0
        for r in range(len(cleaned)-1,-1,-1):
            if cleaned[l]!=cleaned[r]:
                return False
            l+=1
        return True
