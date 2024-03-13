#Naive Solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                while len(stack) > 1:
                    stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                while len(stack) > 1:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    stack.append(num1 - num2)
            elif i == "*":
                while len(stack) > 1:
                    stack.append(int(stack.pop()) * int(stack.pop()))       
            elif i == "/":
                while len(stack) > 1:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    stack.append(num1 // num2)
            else:
                stack.append(int(i))
        return stack.pop()
                