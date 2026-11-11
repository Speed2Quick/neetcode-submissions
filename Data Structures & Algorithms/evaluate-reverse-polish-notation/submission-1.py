class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for token in tokens:
            if token == "+":
                operands.append(operands.pop() + operands.pop())
            elif token == "-":
                second = operands.pop()
                first = operands.pop()
                operands.append(first - second)
            elif token == "*":
                operands.append(operands.pop() * operands.pop())
            elif token == "/":
                second = operands.pop()
                first = operands.pop()
                operands.append(int(first / second))
            else:
                operands.append(int(token))

        return operands[0]