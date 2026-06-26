class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {k: 0 for k in set(list(s) + list(t))}
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        
        for k,v in counts.items():
            if v != 0:
                return False
        return True