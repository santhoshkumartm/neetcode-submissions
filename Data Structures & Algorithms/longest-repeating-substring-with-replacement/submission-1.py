class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        maxl=left=0
        mfreq=0
        if not s : return 0
        # seen[s[left]]=1

        for right in range(len(s)):
                seen[s[right]]=seen.get(s[right],0)+1
                mfreq=max(mfreq,seen[s[right]])
                win=(right-left+1)-mfreq

                while (right-left+1)-mfreq>k:
                    seen[s[left]]-= 1
                    left+=1
                maxl=max(maxl,(right-left+1))
                print(seen,maxl)
        return maxl