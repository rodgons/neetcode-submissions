class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in hash_map.keys():
                return [hash_map[needed], i]
            else:
                hash_map[nums[i]] = i
            
        return Nil