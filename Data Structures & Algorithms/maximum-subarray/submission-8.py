class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        result=nums[0]
        count=0
        for num in nums:
            if count<0:
                count=0
            count+=num
            result=max(result,count)
        return result
