class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = [1] * len(nums)
        auxl, auxr = 1, 1
        while l <= len(nums) - 1:
            result[l] *= auxl
            result[r] *= auxr
            auxl *= nums[l]
            auxr *= nums[r]
            l += 1
            r -= 1
            print(result, l, r, auxl, auxr)

        return result
