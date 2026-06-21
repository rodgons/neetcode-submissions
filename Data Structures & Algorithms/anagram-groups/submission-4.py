class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            key = self.hash_string(s)

            if key not in group:
                group[key] = []

            group[key].append(s)

        res = []

        for k in group.keys():
            res.append(group[k])

        return res

    def hash_string(self, string: str) -> Tuple[int]:
        res = [0] * 26
        for s in string:
            res[ord(s) - ord('a')] += 1

        return tuple(res)