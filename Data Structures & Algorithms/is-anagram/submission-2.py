class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        memo = {}
        for i in range(len(s)):
            memo[s[i]] = memo.get(s[i], 0) + 1
            memo[t[i]] = memo.get(t[i], 0) - 1

        for k in memo.keys():
            if memo[k] != 0:
                return False
        
        return True
        