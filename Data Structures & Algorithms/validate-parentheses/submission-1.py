class Solution:
    closing_to_opening_mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # Opening Bracket
            if c not in self.closing_to_opening_mapping:
                stack.append(c)
            else:
                if not stack :
                    return False
                pop = stack.pop()
                if self.closing_to_opening_mapping[c] != pop:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True