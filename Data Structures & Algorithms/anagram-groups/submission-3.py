class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for _, w in enumerate(strs):
            token = self.tokenize(w)
            if token in groups:
                groups[token].append(w)
            else:
                groups[token] = [w]
        return list(groups.values())

    def tokenize(self, word):
        result = [0] * 26
        for i in range(len(word)):
            result[ord(word[i]) - ord("a")] += 1

        return ";".join(map(str, result))
