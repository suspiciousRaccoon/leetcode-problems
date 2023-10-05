class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack


if __name__ == "__main__":
    test = Solution()
    print(test.isValid("()"), test.isValid("(]"), test.isValid("()[]{}"))
