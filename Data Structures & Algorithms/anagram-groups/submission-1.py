class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}

        for word in strs:
            base = [0] * 26
            for l in word:
                base[ord(l) - 97] += 1
            idx = ','.join(map(str, base))
            memo.setdefault(idx, []).append(word)

        res = [x for x in memo.values()]
        return res