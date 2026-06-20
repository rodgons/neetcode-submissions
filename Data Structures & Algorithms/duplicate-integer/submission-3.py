class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for n in nums:
            if n in dic:
                return True
            dic[n] = True
        return False