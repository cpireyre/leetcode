from collections import deque
class MyStack:

    def __init__(self):
        self.A = deque()
        self.B = deque()

    def __balance__(self):
        while self.A.__len__() > 1:
            self.B.append(self.A.popleft())

    def push(self, x: int) -> None:
        self.A.append(x)
        self.__balance__()

    def pop(self) -> int:
        ret = self.A.popleft()
        self.A, self.B = self.B, self.A
        self.__balance__()
        return ret

    def top(self) -> int:
        return self.A[0]

    def empty(self) -> bool:
        return not self.A and not self.B
# Runtime: 52 ms, faster than 21.80% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14 MB, less than 76.44% of Python3 online submissions for Implement Stack using Queues.


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
