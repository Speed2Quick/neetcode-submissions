class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.min = self.min_stack[-1]
        else:
            self.min = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
