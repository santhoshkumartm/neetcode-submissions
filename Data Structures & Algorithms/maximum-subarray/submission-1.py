class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_so_far=max(max_so_far,current_sum)
        return max_so_far

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

