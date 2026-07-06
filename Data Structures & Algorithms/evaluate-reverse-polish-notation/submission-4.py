class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "*", "-", "/"]
        stack = []
        for t in tokens:
            print(stack)
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack[0]