class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in '+-*/':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(
                    int(eval(str(x1) + char + str(x2)))
                )
            else:
                stack.append(char)
        
        return int(stack[-1])
