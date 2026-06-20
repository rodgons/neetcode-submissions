class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = dict()

        for n in nums:
            if n in hash:
                return True

            hash[n] = True
        return False