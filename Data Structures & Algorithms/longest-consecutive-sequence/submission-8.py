class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset=set(nums)
        count=0
        largec=0
        if nums==[]: return 0
        
        for num in nums:
            if num-1 not in hset:
                count=1
                while num+1 in hset:
                    count+=1
                    num= num+1
            largec=max(largec,count)
        return largec
            