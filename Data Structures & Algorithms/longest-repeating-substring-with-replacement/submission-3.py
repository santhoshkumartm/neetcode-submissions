class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # seen={}
        # maxl=left=0
        # mfreq=0
        if not s : return 0
        # seen[s[left]]=1

        # for right in range(len(s)):
        #         seen[s[right]]=seen.get(s[right],0)+1
        #         mfreq=max(mfreq,seen[s[right]])
        #         win=(right-left+1)-mfreq

        #         while (right-left+1)-mfreq>k:
        #             seen[s[left]]-= 1
        #             left+=1
        #         maxl=max(maxl,(right-left+1))
        #         print(seen,maxl)
        # return maxl

        #Brute Force
        # res=0
        # for  i in range(len(s)):
        #     seen,maxf={},0
        #     for j in range(i,len(s)):
        #         seen[s[j]]=seen.get(s[j],0)+1
        #         maxf=max(maxf,seen[s[j]])
        #         if((j-i+1)-maxf<=k):
        #             res=max(res,(j-i+1))
        # return res

        l=r=0
        charset=set()
        maxf=res=0
        charset=set(s)

        for c in charset:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                while (r-l+1)-count>k:
                    if s[l]==c:
                        count-=1
                    l+=1
                res=max(res,(r-l+1))
        return res


