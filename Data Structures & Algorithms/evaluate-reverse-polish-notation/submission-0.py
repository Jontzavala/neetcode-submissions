class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                right = stack.pop()
                left = stack.pop()
                if tokens[i] == "+":
                    stack.append(left + right)
                elif tokens[i] == "-":
                    stack.append(left - right)
                elif tokens[i] == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(tokens[i]))
        return stack[0]
