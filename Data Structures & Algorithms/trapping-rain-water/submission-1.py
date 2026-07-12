class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        #prefix
        prefix=[0]*n
        prefix[0] = height[0]
        for i in range(n):
            prefix[i]= max(prefix[i-1],height[i])
        
        #suffix
        suffix=[0]*n
        suffix[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]= max(suffix[i+1],height[i])
        

        print('prefix',prefix)
        print('suffix',suffix)


        #contains water amount
        count=0
        for i in range(n-1):
            count+=min(prefix[i], suffix[i]) - height[i]
        return count
