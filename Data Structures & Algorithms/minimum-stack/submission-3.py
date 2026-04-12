class MinStack:

    def __init__(self):
        self.temp = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.minSt.append(val)
        val = min(val, self.temp[-1] if self.temp else val)
        self.temp.append(val)

    def pop(self) -> None:
        self.minSt.pop()
        self.temp.pop()

    def top(self) -> int:
        return self.minSt[-1]

    def getMin(self) -> int:
        return self.temp[-1]