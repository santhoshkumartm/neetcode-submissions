
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for s in strs:
            count=len(s)
            ans+=str(count)+'#'+s
        return ans
        

    def decode(self, s: str) -> List[str]:
        ch=''
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                # ch+=s
                j+=1
            count=int(s[i:j])
            word=s[j+1:j+1+count]
            res.append(word)
            i=j+1+count
        return res
            


# Solution solution = new Solution();
# String encoded_string = solution.encode(strs);

