class Solution:
    def isValid(self, s: str) -> bool:

        bracketmap = {"(":")",
        "{":"}", 
        "[": "]"}
        stack = []

        for b in s:
            if b in bracketmap:
                stack.append(bracketmap.get(b))
            else:
                if not stack or stack[-1] != b:
                    return False
                stack.pop()
        return len(stack) == 0
        
        
        