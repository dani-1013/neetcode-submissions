class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not self.alphaNum(s[left]):
                left += 1
            elif not self.alphaNum(s[right]):
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        # one left pointer at the first index
        # one right pointer at the last index

        # check if the pointers' values are the same
        # while left <= right
            # check if left is non-alphanum
                # left + 1
            # check if right is non-alphanum
                # right - 1
            # if pointers' values == --> keep going
                #left + 1
                #right + 1
            # else return false 
        # return true