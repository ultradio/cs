
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. 
# Each operand may be an integer or another expression.

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while True:
            for i, token in enumerate(tokens):
                if token is "+":                        
                    tokens[i] = int(tokens[i-2]) + int(tokens[i-1])
                elif token is "-":
                    tokens[i] = int(tokens[i-2]) - int(tokens[i-1])
                elif token is "*":
                    tokens[i] = int(tokens[i-2]) * int(tokens[i-1])
                elif token is "/":
                    tokens[i] = int(tokens[i-2]) / int(tokens[i-1])
                else:
                    continue

                del tokens[i-2:i]
                break

            if len(tokens) == 1:
                return int(tokens[0])

sol = Solution()
tokens = ["2","1","+","3","*"]
ans = sol.evalRPN(tokens)
print(ans)

tokens = ["4","13","5","/","+"]
ans = sol.evalRPN(tokens)
print(ans)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
ans = sol.evalRPN(tokens)
print(ans)

