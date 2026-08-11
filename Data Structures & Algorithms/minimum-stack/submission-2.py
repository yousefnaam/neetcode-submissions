class MinStack:

    """
    (2,3,6,1)
    [2,3]
    [2,2]


    """

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else False
        

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else False
        
