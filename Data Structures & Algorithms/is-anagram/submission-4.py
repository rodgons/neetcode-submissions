class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphS, alphT = [0 for i in range(26)], [0 for i in range(26)]
        
        for i in range(len(s)):
            alphS[ord(s[i]) - 97] += 1
            alphT[ord(t[i]) - 97] += 1

        return alphT == alphS