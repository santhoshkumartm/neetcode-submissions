class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        n=len(heights)
        # for i in range(n):
        #     height=heights[i]
        #     rm=i+1
        #     while rm<n and heights[rm]>=height:
        #         rm+=1

        #     lm=i
        #     while lm>=0 and heights[lm]>=height:
        #         lm-=1

        #     rm-=1
        #     lm+=1

        #     res=max(res,height*(rm-lm+1))
        # return res
        # stack=[]
        # lm=[-1]*n
        # for i in range(n):
        #     while stack and heights[stack[-1]]>=heights[i]:
        #         stack.pop()
        #     if stack:
        #         lm[i]=stack[-1]
        #     stack.append(i)

        # stack=[]
        # rm=[n]*n
        # for i in range(n-1,-1,-1):
        #     while stack and heights[stack[-1]]>=heights[i]:
        #         stack.pop()
        #     if stack:
        #         rm[i]=stack[-1]
        #     stack.append(i)
        
        # ma=0
        # for i in range(n):
        #     lm[i]+=1
        #     rm[i]-=1
        #     ma=max(ma,heights[i]*(rm[i]-lm[i]+1))
        # return ma


        stack=[]
        maxA=0
        for i in range(n):
            start=i
            while stack and stack[-1][1]>=heights[i]:
                stackI,stackH=stack.pop()
                maxA=max(maxA,stackH*(i-stackI))
                start=stackI
            stack.append((start,heights[i]))

        for i,h in stack:
            maxA=max(maxA,h*(len(heights)-i))
        return maxA
            