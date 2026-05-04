class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for x in tokens:
            if x == '+' and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif x == '-' and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif x == '*' and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)   
            elif x == '/' and stack:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append((int)(x))
        
        return stack[-1]
        