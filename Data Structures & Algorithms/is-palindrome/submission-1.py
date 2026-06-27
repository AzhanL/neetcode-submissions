class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
            elif not self.isAlphaNum(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                # Matches character
                l += 1
                r -= 1
        return True

    def isAlphaNum(self, c: str):
        return (
            (ord('A') <= ord(c.lower()) <= ord('Z')) or
            (ord('a') <= ord(c.lower()) <= ord('z')) or
            (ord('0') <= ord(c.lower()) <= ord('9')) 
        )