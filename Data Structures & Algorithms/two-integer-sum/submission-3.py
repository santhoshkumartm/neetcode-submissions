class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap={}

        # for i,n in enumerate(nums):
        #     diff=target-n
        #     if diff in prevMap:
        #         return [prevMap[diff],i]
        #     prevMap[n]=i

        # seen={}

        # for i ,n in enumerate(nums):
        #     seen[n]=i

        # for i,n in enumerate(nums):
        #     diff=target-nums[i]
        #     if diff in seen and seen[diff]!=i:
        #         return [i,seen[diff]]
        # return []

        arr=[]

        for i,num in enumerate(nums):
            arr.append([num,i])
        # print(arr)

        left,right=0,len(arr)-1
        arr.sort()
        while left<right:
            cur=arr[left][0] + arr[right][0]
            if cur==target:
                return[
                    min(arr[left][1],arr[right][1]),
                    max(arr[left][1],arr[right][1]),
                ]
            elif(cur<target):
                left+=1
            else:
                right-=1
        return[]
            