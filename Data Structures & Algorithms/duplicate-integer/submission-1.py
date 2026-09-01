class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen=set(nums)
        return len(nums)!=len(set(nums))
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # for num in nums:
            