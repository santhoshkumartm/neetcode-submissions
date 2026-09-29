class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res=[]
        # bas=set(nums)
        # for i in range(len(nums)):
        #     if i+1 not in bas:
        #         res.append(i+1)
        # return res
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Step 2: collect missing
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res