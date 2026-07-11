class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=0
        l=len(numbers)-1

        while r<l:
            count=numbers[r]+numbers[l] 
            print(count,numbers[r],numbers[l])
            if count !=target:
                if count> target:
                    l-=1
                else:
                    r+=1
            else:
                return [r+1,l+1]
