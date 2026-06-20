class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, v in enumerate(nums):
            res = target - v
            if res in memo:
                return [memo[res], i]
            memo[v] = i