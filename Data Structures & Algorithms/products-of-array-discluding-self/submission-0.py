class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right = 1,1
        result = [1 for i in range(len(nums))]
        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            result[i] *= left
            result[j] *= right
            left *= nums[i]
            right *= nums[j]
        return result