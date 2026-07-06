class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "*", "-", "/"]
        stack = []
        for t in tokens:
            print(stack)
            if t in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                match t:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(a/b)
            else:
                stack.append(t)
        return int(stack[0])