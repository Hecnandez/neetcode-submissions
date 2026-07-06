class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            # char is an opening bracket (add to stack)
            if c in pairs.values():
                stack.append(c)
            # char is a closing bracket
            elif c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0