class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        # count=0
        # for num in nums:
        #     count=sum(1 for i in nums if i==num)
        #     if count>n//2:
        #         return num

        freq={}
        val=0
        max_count=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
            max_count=max(max_count,freq[num])
            if max_count > n//2:
                return num