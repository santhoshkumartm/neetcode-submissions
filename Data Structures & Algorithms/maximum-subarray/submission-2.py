class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_so_far = nums[0]
        # current_sum = nums[0]

        # for num in nums[1:]:
        #     current_sum=max(num,current_sum+num)
        #     max_so_far=max(max_so_far,current_sum)
        # return max_so_far

        # n,res=len(nums),nums[0]

        # for  i in range(n):
        #     cur=0
        #     for j in range(i,n):
        #         cur+=nums[j]
        #         res=max(res,cur)
        # return res


        # def dfs(i,flag):
        #     if i==len(nums)-1:
        #         return max(0,nums[i]) if flag else nums[i]
        #     if flag:
        #         return max(0,nums[i]+dfs(i+1,True))
        #     return(max(dfs(i+1,False),nums[i]+dfs(i+1,True)) )
        # return(dfs(0,False))

        # n=len(nums)

        # dp=[[0]*2 for _ in range(n)]
        # dp[n-1][0]=dp[n-1][1]=nums[n-1]

        # for i in range(n-2,-1,-1):
        #     dp[i][1]=max(nums[i],nums[i]+dp[i+1][1])
        #     dp[i][0]=max(dp[i+1][0],dp[i][1])
        
        # return dp[0][0]


        
        maxs,cur=nums[0],0

        for num in nums:
            if cur<=0:
                cur=0
            cur+=num
            maxs=max(maxs,cur)
        return maxs
        
        











