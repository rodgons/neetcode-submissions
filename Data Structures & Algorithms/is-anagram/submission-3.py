class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        memo = [0] * 26

        for i in range(0, len(s)):
            memo[ord(s[i]) - 97] += 1
            memo[ord(t[i]) - 97] -= 1

        print(memo)

        for v in memo:
            if v != 0:
                return False

        return True