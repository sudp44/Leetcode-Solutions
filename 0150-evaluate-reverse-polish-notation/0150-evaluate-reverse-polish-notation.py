class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if self.isOperator(token):
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand
                result = self.applyOperator(token, a, b)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()
    
    def isOperator(self, token: str) -> bool:
        return token in {'+', '-', '*', '/'}
    
    def applyOperator(self, operator: str, a: int, b: int) -> int:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(a / b)   # truncates toward zero, same as Java's integer division     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna