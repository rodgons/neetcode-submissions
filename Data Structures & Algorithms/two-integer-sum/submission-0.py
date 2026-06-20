class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(0, len(nums)):
            opt = target - nums[i]
            if opt in memo:
                return [memo[opt], i]
            memo[nums[i]] = i
        return []