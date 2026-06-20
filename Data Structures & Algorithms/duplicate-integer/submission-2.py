class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = {}

        for v in nums:
            if v in memo:
                return True
            memo[v] = True
        return False