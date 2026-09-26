class MinStack:

    def __init__(self):
        self.stack = []
        self.min_seen = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_seen:
            self.min_seen.append(val)
        else:
            self.min_seen.append(min(val, self.min_seen[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_seen.pop() 
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_seen[-1]
