class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        l=0
        seen={}
        # seen[s[l]]=0
        count=0
        for r,c in enumerate(s):
            if c in seen and seen[c]>=l:
                l=seen[c]+1
            seen[c]=r
            count=max(count,r-l+1)
        return count
        # print(seen)
            
















