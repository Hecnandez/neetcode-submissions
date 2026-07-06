class MinStack:
    def __init__(self):
        self.elements = []

    def push(self, val: int) -> None:
        self.elements.append(val)

    def pop(self) -> None:
        return self.elements.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        smallest = self.elements[0]
        for e in self.elements:
            smallest = min(smallest, e)
        return smallest