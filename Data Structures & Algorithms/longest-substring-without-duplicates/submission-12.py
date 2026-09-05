class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        
        # hset = set()
        # l, r = 0, 1
        # n = len(s)
        # maxl = 1  
        # hset.add(s[l])
        
        # while r < n:
        #     if s[r] in hset:
        #         while s[r] in hset:
        #             hset.remove(s[l])
        #             l += 1
        #     hset.add(s[r])
        #     maxl = max(maxl, r - l + 1)
        #     r += 1
        
        # return maxl

        # seen={}
        # l,r=0,1
        # maxl=1
        # n = len(s)
        # seen[s[l]]=l

        # while r<n:
        #     if s[r] in seen:
        #         l=max(l,seen[s[r]]+1)
        #     seen[s[r]]=r
        #     maxl = max(maxl, r - l+1)
        #     r+=1
        # return maxl

        #hashmap
        # seen={}
        val=0
        n=len(s)
        l=0
        # for r in range(0,n):
        #     if s[r] in seen:
        #         l=max(l,seen[s[r]]+1)
        #     seen[s[r]]=r
        #     val=max(val,r-l+1)
        # return val

        #Brute Force
        # for i in range(n):
        #     charset=set()
        #     for j in range(i,n):
        #         if s[j] in charset:
        #             break
        #         charset.add(s[j])
        #         val=max(val,len(charset))

        # return val

        #sliding window
        chatset=set()
        for r in range(n):
            while s[r] in chatset:
                chatset.remove(s[l])
                l+=1
            chatset.add(s[r])
            val=max(val,r-l+1)
        return val



