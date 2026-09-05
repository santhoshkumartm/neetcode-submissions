class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left=0
        # bestp=0
        
        # for right in range(1,len(prices)):
        #     if prices[left]<prices[right]:
        #         bestp=max(bestp,prices[right]-prices[left])
        #     else:
        #         left=right
        # return bestp

        l=res=0
        for r in range(1,len(prices)):
            if prices[l]<prices[r]:
                res=max(res,(prices[r]-prices[l]))
            else:
                l=r
        return res
            

    