from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(nums[::-1])
        # res=[]
        # nums.sort()

        # for i in range(len(nums)-1):
        #     curr=nums[i]
        #     r=i+1
        #     l=len(nums)-1

        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     while r<l:
        #         total=nums[r]+nums[l]+curr
        #         if total>0:
        #             l-=1
        #         elif total<0:
        #             r+=1
        #         else:
        #             res.append([nums[r],nums[l],curr])
        #             while r<l and nums[r]==nums[r+1]:
        #                 r+=1
        #             while r<l and nums[l]==nums[l-1]:
        #                 l-=1
        #             r+=1
        #             l-=1
        # return res            



        # res=set()
        # n=len(nums)
        # nums.sort()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 tmp=[nums[i],nums[j],nums[k]]
        #                 res.add(tuple(tmp))
        # return[list(i) for i in res]


        nums.sort()
        count=defaultdict(int)
        for num in nums:
            count[num]+=1

        res=[]
        n=len(nums)
        for i in range(n):
            count[nums[i]]-=1

            if i and nums[i]==nums[i-1]:
                    continue

            for j in range(i+1,n):
                count[nums[j]]-=1
                if j-1>i and nums[j]==nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if count[target]>0:
                    res.append([nums[i],nums[j],target])
                
            for j in range(i+1,n):
                count[nums[j]]+=1

        return res