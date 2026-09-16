class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1
        for i in range(1,n+1):
            tmp=one+two
            one=two
            two=tmp
        return one
