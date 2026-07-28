class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for letter in range(len(s)):
            count[ord(s[letter]) - ord("a")] += 1
            count[ord(t[letter]) - ord("a")] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True