class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: # sort by position in decreasing order
            t = (target - p) / s
            if len(stack) == 0 or (len(stack) >= 1 and t > stack[-1]):
                stack.append(t)
        return len(stack)