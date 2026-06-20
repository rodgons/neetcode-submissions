class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            v = target - nums[i]
            if v in memo:
                return [memo[v], i]
            memo[nums[i]] = i
        return []