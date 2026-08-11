class Solution:
    def isValid(self, s: str) -> bool:
        """
        Every open bracket is closed by the same type of close bracket
        Open brackets are closed in the correct order
        Every close bracket has a corresponding open bracket of the same type


        if its an opening bracket, we append to stack, if its a closing bracket 
        we check hashmap and see if top of stack ==
        
        ([{}]) 
        stack = [(,[,{]
        
        """

        bracketmap = {"}":"{", ")":"(", "]":"["}

        stack = []

        for bracket in s:
            if bracket in bracketmap.values():
                stack.append(bracket)
            elif stack and bracket in bracketmap.keys() and stack[-1] == bracketmap.get(bracket):
                stack.pop()
            else:
                return False
            
        return not stack


                