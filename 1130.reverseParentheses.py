class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                buf = ''
                while stack[-1] != '(':
                    buf += stack.pop()
                stack.pop()
                for b_c in buf:
                    stack.append(b_c)
            else:
                stack.append(c)

        return ''.join(stack)