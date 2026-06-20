class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        aux = [[] for _ in range(len(nums)+1)]
        result = []

        for n in nums:
            group[n] = nums.count(n)
        for key, v in group.items():
            aux[v].append(key)
        for i in range(len(aux) - 1, 0, -1):
            result.extend(aux[i])
            if len(result) >= k:
                break

        return result[:k]

