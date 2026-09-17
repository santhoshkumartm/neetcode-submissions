class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        # for s in strs:
        #     sortedS=''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())

        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())

        # if strs=="":
        #     return ""

        # seen={}
        # for s in strs:
        #     c=''.join(sorted(s))
        #     if c  in seen:
        #         seen[c].append(s)
        #     else:
        #         seen[c]=[s]
        # return list(seen.values())

