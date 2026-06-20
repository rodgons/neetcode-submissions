class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphaS, alphaT = [0 for _ in range(26)], [0 for _ in range(26)]

        for i in range(len(s)):
            alphaS[ord(s[i]) - 97] += 1
            alphaT[ord(t[i]) - 97] += 1
    
        return alphaS == alphaT