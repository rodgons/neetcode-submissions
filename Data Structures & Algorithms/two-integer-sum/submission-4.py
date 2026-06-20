class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            s = target - nums[i]
            if s in memo:
                return [memo[s], i]
            memo[nums[i]] = i
        return []
        