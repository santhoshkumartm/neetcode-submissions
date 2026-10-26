class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        for i in range(len(arr)):
            l=arr[i]
            for j in range(i,len(arr)):
                l=max(l,arr[j])
            arr[i]=l
        arr.append(-1)
        return arr[1:]
