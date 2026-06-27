class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                # Matches character
                l += 1
                r -= 1
        return True

    def isAlphaNum(self, c: str):
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9')) 
        )