class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        maxi=nums[0]
        count=0
        for num in nums:
            count=max(num,count+num)
            maxi=max(maxi,count)
        return maxi








