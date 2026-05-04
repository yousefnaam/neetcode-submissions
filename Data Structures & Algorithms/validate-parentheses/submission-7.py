class Solution:
    def isValid(self, s: str) -> bool:

        bracketmap = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        stack = []

        for c in s:
            if c in bracketmap:
                stack.append(bracketmap.get(c))
            else:
                if not stack or c != stack.pop():
                    return False
        
        return True if not stack else False