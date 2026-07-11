class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(nums[::-1])
        res=[]
        nums.sort()

        for i in range(len(nums)-1):
            curr=nums[i]
            r=i+1
            l=len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while r<l:
                total=nums[r]+nums[l]+curr
                if total>0:
                    l-=1
                elif total<0:
                    r+=1
                else:
                    res.append([nums[r],nums[l],curr])
                    while r<l and nums[r]==nums[r+1]:
                        r+=1
                    while r<l and nums[l]==nums[l-1]:
                        l-=1
                    r+=1
                    l-=1
        return res            