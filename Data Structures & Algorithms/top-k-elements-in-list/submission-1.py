class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            group[n] = 1 + group.get(n, 0)
        for key, v in group.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res

        return res


