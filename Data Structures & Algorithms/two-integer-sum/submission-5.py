class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        d = {}
        d2 = {}
        c = 0
        for i, n in enumerate(nums):
            d2[n] = i
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if d2[(target - nums[i])] != i:
                    return [i, d2[(target - nums[i])]]
        return []