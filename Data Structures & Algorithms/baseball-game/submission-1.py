class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []
        ans: int = 0
        for op in operations:
            if op == "+":
                ans += stack[-2] + stack[-1]
                stack.append(stack[-2] + stack[-1])
            elif op == "C":
                ans -= stack.pop()
            elif op == "D":
                ans += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else:
                ans += int(op)
                stack.append(int(op))
        return ans