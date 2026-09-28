class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i,ch in enumerate(s):
            seen[ch]=seen.get(ch,0)+1
        print(seen)
        i=0
        for ch in s:
            if seen[ch]==1:
                print(seen[ch])
                return i
            i+=1
        return -1
