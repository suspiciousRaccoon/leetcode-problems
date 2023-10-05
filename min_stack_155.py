from collections import deque


class MinStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(15)
    obj.pop()
    obj.push(123)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)
