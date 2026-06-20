class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for i, n in enumerate(nums):
            missing = target - n

            if missing in n_map.keys():
                return [n_map[missing], i]

            n_map[n] = i

        return []