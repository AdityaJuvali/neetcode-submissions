class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in nums:
            if i not in hashset:
                hashset[i]=0
            else:
                return True
        return False

        
                