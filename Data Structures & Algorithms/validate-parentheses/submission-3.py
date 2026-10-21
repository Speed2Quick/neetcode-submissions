class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[s] = []
        for bracket in s:
            if bracket == "(":
                stack.append(")")
            elif bracket == "[":
                stack.append("]")
            elif bracket == "{":
                stack.append("}")
            else:
                if len(stack) == 0 or bracket != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
