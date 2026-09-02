class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res[i] = prod
        # return res

        # zero_count,prod=0,1

        # for num in nums:
        #     if num:
        #         prod*=num
        #     else:
        #         zero_count+=1
        # if zero_count>1:return [0]*len(nums)

        # res=[0]*len(nums)
        # for i,c in enumerate(nums):
        #     if zero_count:res[i]=0 if c else prod
        #     else: res[i]=prod//c
        # return res

        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        res=[0]*n

        prefix[0]=suffix[n-1]=1
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]
        # print(prefix,suffix)
        for i in range(n):
            res[i]=prefix[i]*suffix[i]
        return res
        #sufffix
        # for i in range(n-2,-1,-1):


        