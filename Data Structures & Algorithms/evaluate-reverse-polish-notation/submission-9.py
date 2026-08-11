class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        input could be num or operators
        use stack, once we get an operator, 
        
        [1,2]
        """

        stack = []

        for num in tokens:
            if num == "+":
                num1,num2 = stack.pop(), stack.pop()
                stack.append(num2+num1)
            elif num == "-":
                num1,num2 = stack.pop(), stack.pop()
                stack.append(num2-num1)
            elif num == "*":
                num1,num2 = stack.pop(), stack.pop()
                stack.append(num2*num1)
            elif num == "/":
                num1,num2 = stack.pop(), stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(num))
        return stack[-1]