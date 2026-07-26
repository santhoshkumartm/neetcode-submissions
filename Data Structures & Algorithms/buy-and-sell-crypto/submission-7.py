class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        bestp=0
        
        for right in range(1,len(prices)):
            if prices[left]<prices[right]:
                # print(prices[right]-prices[left])
                bestp=max(bestp,prices[right]-prices[left])
            
            else:
                left=right
        return bestp
            

    