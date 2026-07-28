class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hashmap = {}
        t_hashmap = {}

        for letter in s:
            if letter not in s_hashmap:
                s_hashmap[letter] = 1
            else:
                s_hashmap[letter] += 1

        for letter in t:
            if letter not in t_hashmap:
                t_hashmap[letter] = 1
            else:
                t_hashmap[letter] += 1
        
        if s_hashmap == t_hashmap:
            return True
        return False