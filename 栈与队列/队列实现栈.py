from collections import deque

class MyStack:

    def __init__(self):
        self.dq1 = deque()
        self.dq2 = deque()

    def push(self, x: int) -> None:
        self.dq2.append(x)
        while self.dq1:
            self.dq2.append(self.dq1.popleft())
        
        self.dq1, self.dq2 = self.dq2, self.dq1

    def pop(self) -> int:
        return self.dq1.popleft()

    def top(self) -> int:
        return self.dq1[0]        

    def empty(self) -> bool:
        return not self.dq1
