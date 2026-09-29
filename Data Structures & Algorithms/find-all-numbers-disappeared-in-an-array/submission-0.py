class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        bas=set(nums)
        for i in range(len(nums)):
            if i+1 not in bas:
                res.append(i+1)
        return res
        