class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[0]
        # while l<=r:
        #     if nums[l]<nums[r]:
        #         res=min(res,nums[l])
        #         break

        #     m = (l + r) // 2
        #     res=min(res,nums[m])
        #     if nums[m] >=nums[l]:
        #         l=m+1
        #     else:
        #         r=m-1
        # return res
            






        # while l<=r:
        #     if nums[l]<nums[r]:
        #         res=min(res,nums[l])
        #         break
        #     m=(l+r)//2
        #     res=min(res,nums[m])
        #     if nums[l]<=nums[m]:
        #         l=m+1
        #     else:
        #         r=m-1
        # return res








        # while l<=r:
        #     if nums[l]<nums[r]:
        #         res=min(res,nums[l])
        #         break
        #     m=l+(r-l)//2
        #     res=min(res,nums[m])
        #     if nums[m]>=nums[l]:
        #         l=m+1
        #     else:
        #         r=m-1
        # return res





        while l<r:
            m=l+(r-l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]