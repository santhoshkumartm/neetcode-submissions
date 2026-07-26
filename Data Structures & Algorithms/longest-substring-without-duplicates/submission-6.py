class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        hset=set()
        l,r=0,1
        n=len(s)
        maxl=1
        hset.add(s[l])
        while r<n:
            
            if s[r] in hset:
                # print(len(hset))
                
                
                while s[r] in hset:
                    print(s[l])
                    hset.remove(s[l])
                    l+=1
                
            hset.add(s[r])
            maxl=max(maxl,r-l+1)
            r+=1
        return maxl

