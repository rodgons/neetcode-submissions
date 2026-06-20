class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = [0 for _ in range(26)]

        for i in range(len(s)):
            letters[ord(s[i])-97] += 1
            letters[ord(t[i])-97] -= 1
        
        for x in letters:
            if x != 0:
                return False
        return True