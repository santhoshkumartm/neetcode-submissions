from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hset=set(nums)
        # count=0
        # largec=0
        # if nums==[]: return 0
        
        # for num in nums:
        #     if num-1 not in hset:
        #         count=1
        #         while num+1 in hset:
        #             count+=1
        #             num= num+1
        #     largec=max(largec,count)
        # return largec


        # longest=0
        # for num in nums:
        #     if num-1 not in hset:
        #         length=1
        #         while num+length in hset:
        #             length+=1
        #         longest=max(length,longest)
        # return longest

        # mp = defaultdict(int)
        # res=0
        # for num in nums:
        #     if not mp[num]:
        #         mp[num]=mp[num-1]+mp[num+1]+1
        #         mp[num - mp[num-1]]=mp[num]
        #         mp[num + mp[num+1]]=mp[num]
        #         res=max(res,mp[num])

        # return res

        
        seen=set(nums)
        larger=0
        for num in nums:
            # count=0
            if num-1 not in seen:
                count=1
                while count+num in seen:
                    count+=1
                larger=max(count,larger)
        return larger




