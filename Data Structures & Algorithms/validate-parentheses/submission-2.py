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
                if stack and stack[-1] == self.closing_to_opening_mapping[c]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True