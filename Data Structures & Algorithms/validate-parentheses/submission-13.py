class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        bracketmap = {"}":"{", 
        "]":"[", 
        ")":"("}

        """
        stack: ( [  { } 

        """

        for bracket in s:
            if bracket in bracketmap.values():
                stack.append(bracket)
            else:
                if not stack or bracketmap[bracket] != stack.pop():
                    return False
        return True if len(stack) == 0 else False

        
        