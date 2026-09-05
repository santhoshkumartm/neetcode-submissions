class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l=0
        # r=len(heights)-1
        # lar=0

        # while l<r:
        #     water=min(heights[l],heights[r])*(r-l)
        #     lar=max(lar,water)
        #     if heights[l]<heights[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return lar
            
        # res=0
        # n=len(heights)
        # for i in range(n):

        #     for j in range(n-1,-1,-1):
        #         res=max(res,min(heights[i],heights[j])*(j-i))
        # return res

        l,r=0,len(heights)-1
        res=0
        while l<r:
            res=max(res,min(heights[l],heights[r])*(r-l));
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res