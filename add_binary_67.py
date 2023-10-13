from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])


class NormalSolution:
    def addBinary(self, a: str, b: str) -> str:
        result = deque()
        carry = 0

        for i in range(-1, -(max(len(a), len(b))+1), -1):
            digit_a = int(a[i]) if i >= -len(a) else 0
            digit_b = int(b[i]) if i >= -len(b) else 0

            total = digit_a + digit_b + carry
            digit = total % 2
            result.appendleft(digit)
            carry = total // 2
        if carry:
            result.appendleft(1)

        return "".join(map(lambda x: str(x), result))


class BadSolution:  # which was obviously mine
    def addBinary(self, a: str, b: str) -> str:
        result = deque()
        carry = 0

        for i in range(-1, -(max(len(a), len(b))+1), -1):
            digit_a = a[i] if i >= -len(a) else "0"
            digit_b = b[i] if i >= -len(b) else "0"

            if digit_a == "1" and digit_b == "1":
                if carry:
                    result.appendleft("1")
                else:
                    result.appendleft("0")
                carry = 1
            elif "1" in {digit_a, digit_b} and "0" in {digit_a, digit_b}:
                if carry:
                    result.appendleft("0")
                else:
                    result.appendleft("1")
                    carry = 0
            else:
                if carry:
                    result.appendleft("1")
                    carry = 0
                else:
                    result.appendleft("0")
        if carry:
            result.appendleft("1")
        return "".join(result)
